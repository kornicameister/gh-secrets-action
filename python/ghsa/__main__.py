#!/usr/bin/env python3
import base64
import typing as t

import requests as r
from nacl import encoding, public

def main(
        secrets: t.Dict[str, str],
        gh_repository: str,
        gh_token: str,
) -> None:
    ...


def encrypt(p_key: str, secret_value: str) -> str:
    public_key = public.PublicKey(
        p_key.encode('utf-8'),
        encoding.Base64Encoder(),
    )

    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(secret_value.encode('utf-8'))

    return base64.b64encode(encrypted).decode('utf-8')


def get_secret_public_key(gh_repo: str, gh_token: str) -> t.Dict[str, str]:
    # GET /repos/:owner/:repo/actions/secrets/public-key
    return r.get(
        f'https://api.github.com/repos/{gh_repo}/actions/secrets/public-key',
        headers={
            'Authorization': f'token {gh_token}',
            'Content-Type': 'application/json',
        },
    ).json()


if __name__ == '__main__':
    import argparse
    import json
    import sys

    parser = argparse.ArgumentParser(
        prog='gh-secrets-action',
        description=(
            'Action sets up as many secrets as you '
            'wish against a repo of your choice'
        ),
    )
    parser.add_argument('secrets', type=json.loads)
    parser.add_argument('--repo', type=str, required=True)
    parser.add_argument('--token', type=str, required=True)

    args = parser.parse_args(sys.argv[1:])
    if not args:
        parser.print_usage()
        sys.exit(1)
    else:
        main(
            args.stack_output,
            gh_repository=args.repo,
            gh_token=args.token,
        )
        sys.exit(0)
