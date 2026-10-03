import argparse
import json


def main():
    parser = argparse.ArgumentParser(description='Manual local PC demo production; publishing disabled')
    sub = parser.add_subparsers(dest='action', required=True)
    sub.add_parser('setup')
    sub.add_parser('doctor')
    sub.add_parser('status', help='Inspect the local installation and latest draft; no downloads or inference')
    sub.add_parser('audit-git')
    run = sub.add_parser('run')
    run.add_argument('--gpu-id', type=int, default=-1, help='-1 lets the official app select a Vulkan GPU')
    verify = sub.add_parser('verify')
    verify.add_argument('--run', help='Run directory; defaults to the latest completed local draft')
    args = parser.parse_args()
    if args.action == 'status':
        from .status import local_status
        print(json.dumps(local_status(), indent=2))
    elif args.action == 'audit-git':
        from .audit import audit_git
        print(json.dumps(audit_git(), indent=2))
    elif args.action == 'setup':
        from .setup_runtime import setup
        setup()
    elif args.action == 'doctor':
        from .setup_runtime import doctor
        print(json.dumps(doctor(), indent=2))
    elif args.action == 'run':
        from .pipeline import run_demo
        print(run_demo(args.gpu_id))
    elif args.action == 'verify':
        from .verify import verify_run
        from .common import resolve_run
        print(json.dumps(verify_run(resolve_run(args.run)), indent=2))


if __name__ == '__main__':
    main()
