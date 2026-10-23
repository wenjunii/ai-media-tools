import argparse
import json


def main():
    parser = argparse.ArgumentParser(description='Manual local PC demo production; publishing disabled')
    sub = parser.add_subparsers(dest='action', required=True)
    sub.add_parser('setup')
    sub.add_parser('doctor')
    sub.add_parser('status', help='Inspect the local installation and latest draft; no downloads or inference')
    sub.add_parser('audit-git')
    for action in ('run', 'preflight'):
        command = sub.add_parser(action, help=('Produce a local draft' if action == 'run'
                                             else 'Check local inputs and dependencies without inference or downloads'))
        command.add_argument('--storyboard', help='Edited local storyboard JSON; the supported six-scene template is validated')
        command.add_argument('--input', dest='input_image', help='Local opaque PNG/JPEG artwork, 64–1024 pixels per side; preserved unchanged')
        command.add_argument('--library-file', help='Local library JSON; defaults to the checkout public/library.json, with no network request')
        if action == 'run':
            command.add_argument('--gpu-id', type=int, default=-1, help='-1 lets the official app select a Vulkan GPU')
        else:
            command.add_argument('--json', action='store_true')
    revise = sub.add_parser('revise', help='Make a new draft from preserved app output without inference or downloads')
    revise.add_argument('--run', help='Source run; defaults to the latest completed draft')
    revise.add_argument('--storyboard', help='Edited storyboard JSON; defaults to the source run storyboard')
    history = sub.add_parser('history', help='List local completed and failed runs')
    history.add_argument('--limit', type=int, default=20)
    history.add_argument('--json', action='store_true')
    verify = sub.add_parser('verify')
    verify.add_argument('--run', help='Run directory; defaults to the latest completed local draft')
    package = sub.add_parser('package', help='Create a local creator-review package from a verified draft')
    package.add_argument('--run', help='Source run; defaults to the latest completed draft')
    review = sub.add_parser('review', help='Import an explicit creator review for the exact saved draft')
    review.add_argument('--run', help='Reviewed run; defaults to the latest completed draft')
    review.add_argument('--review-file', required=True, help='review.json downloaded from the local package review page')
    args = parser.parse_args()
    if args.action == 'preflight':
        from .preflight import inspect_preflight, format_preflight
        result = inspect_preflight(args.storyboard, args.input_image, args.library_file)
        print(json.dumps(result, indent=2) if args.json else format_preflight(result))
        if not result['passed']:
            raise SystemExit(2)
    elif args.action == 'status':
        from .status import local_status
        print(json.dumps(local_status(), indent=2))
    elif args.action == 'history':
        from .history import local_history, format_history
        result = local_history(args.limit)
        print(json.dumps(result, indent=2) if args.json else format_history(result))
    elif args.action == 'audit-git':
        from .audit import audit_git
        print(json.dumps(audit_git(), indent=2))
    elif args.action == 'package':
        from .common import resolve_run
        from .package import export_package
        print(json.dumps(export_package(resolve_run(args.run)), indent=2))
    elif args.action == 'review':
        from .common import resolve_run
        from .creator_review import import_creator_review
        print(json.dumps(import_creator_review(resolve_run(args.run), args.review_file), indent=2))
    elif args.action == 'setup':
        from .setup_runtime import setup
        setup()
    elif args.action == 'doctor':
        from .setup_runtime import doctor
        print(json.dumps(doctor(), indent=2))
    elif args.action == 'run':
        from .pipeline import run_demo
        print(run_demo(args.gpu_id, args.storyboard, args.input_image, args.library_file))
    elif args.action == 'revise':
        from .common import resolve_run
        from .revisions import revise_demo
        print(revise_demo(resolve_run(args.run), args.storyboard))
    elif args.action == 'verify':
        from .verify import verify_run
        from .common import resolve_run
        print(json.dumps(verify_run(resolve_run(args.run)), indent=2))


if __name__ == '__main__':
    main()
