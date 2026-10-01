"""Reserve a daily Gmail send, then record its returned message ID.

This module does not send mail itself. The connected Gmail tool performs the send.
A process crash after reservation requires mailbox reconciliation, never a resend.
"""

from pathlib import Path
from html import escape
from .configuration import load_config, require_recipient
from .publication import verify_sync

from .report import verify_report
from .storage import ROOT, locked, now, read_json, report_date, write_json


def prepare(day, root=ROOT):
    root = Path(root)
    day = report_date(day)
    with locked(root):
        manifest = verify_report(day, root)
        receipt_path = root / "state/deliveries" / (day + ".json")
        receipt = read_json(receipt_path)
        if receipt:
            if receipt["status"] == "sent":
                return {"status": "already-sent", "message_id": receipt["message_id"]}
            raise RuntimeError("Send already reserved or outcome uncertain. Reconcile Sent mail before any further action; do not resend.")
        require_recipient(manifest["recipient"])
        config = load_config(root)
        publication = None
        if config.get("github_sync", {}).get("required_before_email"):
            publication = verify_sync(day, root)
        folder = root / "reports" / day
        plain = (folder / "report.md").read_text()
        html = (folder / "report.html").read_text()
        payload = {"to": manifest["recipient"], "subject": manifest["subject"],
                   "payload": {"mime_type": "multipart/alternative", "parts": [
                       {"mime_type": "text/plain", "charset": "UTF-8", "body": {"content": plain}},
                       {"mime_type": "text/html", "charset": "UTF-8", "body": {"content": html}},
                   ]}}
        if len(html.encode("utf-8")) > config.get("email_inline_max_bytes", 90_000):
            report = read_json(folder / "report.json")
            counts = f'{manifest["profile_count"]} full profiles; {manifest.get("lead_count", 0)} additional discoveries.'
            summary = f'AI Media Scout — {day}\n\n{report["summary"]}\n\n{counts}\nThe complete edition is attached in HTML and Markdown.'
            overview = f'<h1>AI Media Scout · {day}</h1><p>{escape(report["summary"])}</p><p>{escape(counts)}</p><p>The complete edition is attached in HTML and Markdown.</p>'
            payload["payload"] = {"mime_type": "multipart/mixed", "parts": [
                {"mime_type": "multipart/alternative", "parts": [
                    {"mime_type": "text/plain", "charset": "UTF-8", "body": {"content": summary}},
                    {"mime_type": "text/html", "charset": "UTF-8", "body": {"content": overview}}]},
                {"mime_type": "text/html", "charset": "UTF-8", "content_disposition": "attachment",
                 "filename": f"ai-media-scout-{day}.html", "body": {"content": html}},
                {"mime_type": "text/markdown", "charset": "UTF-8", "content_disposition": "attachment",
                 "filename": f"ai-media-scout-{day}.md", "body": {"content": plain}}]}
        output = root / "state/outbox" / (day + ".json")
        write_json(output, payload)
        receipt = {"report_date": day, "status": "reserved", "reserved_at": now(),
                                  "recipient": manifest["recipient"], "subject": manifest["subject"],
                                  "report_sha256": manifest["sha256"][f"reports/{day}/report.html"],
                                  "transport": "connected-gmail"}
        if publication:
            receipt.update(github_commit=publication["commit"], github_report_url=publication["report_url"])
        write_json(receipt_path, receipt)
        return {"status": "reserved", "payload_path": str(output), "subject": manifest["subject"]}


def record(day, message_id, root=ROOT, reconciled=False):
    root = Path(root)
    day = report_date(day)
    if not isinstance(message_id, str) or not message_id.strip() or len(message_id) > 256:
        raise ValueError("Record the Gmail message ID returned by the successful send or Sent-mail reconciliation")
    with locked(root):
        manifest = verify_report(day, root)
        path = root / "state/deliveries" / (day + ".json")
        receipt = read_json(path)
        if not receipt:
            if not reconciled:
                raise ValueError("No send reservation; reserve before sending")
            receipt = {"report_date": day, "transport": "connected-gmail",
                       "recipient": manifest["recipient"], "subject": manifest["subject"],
                       "report_sha256": manifest["sha256"][f"reports/{day}/report.html"]}
        if receipt.get("message_id") and receipt["message_id"] != message_id:
            raise ValueError("A different message ID was already recorded; inspect the mailbox")
        if receipt["report_sha256"] != manifest["sha256"][f"reports/{day}/report.html"]:
            raise ValueError("Receipt does not match the sealed report")
        receipt.update(status="sent", message_id=message_id.strip(), recorded_at=now(),
                       reconciled=reconciled, meaning="Gmail accepted the send; independent inbox arrival is not implied")
        write_json(path, receipt)
        return receipt


def uncertain(day, root=ROOT):
    root = Path(root)
    day = report_date(day)
    with locked(root):
        path = root / "state/deliveries" / (day + ".json")
        receipt = read_json(path)
        if not receipt or receipt["status"] == "sent":
            raise ValueError("Only a reserved send can be marked uncertain")
        receipt.update(status="uncertain", recorded_at=now(),
                       meaning="Do not resend automatically; inspect Sent mail and resolve the outcome")
        write_json(path, receipt)
        return receipt
