#!/usr/bin/env python3
import base64
import typing as t

from nacl import encoding, public
import requests as r


def main(
        secrets: t.Dict[str, str],
        gh_repository: str,
        gh_token: str,
) -> None:
    encryption_key, encryption_key_id = get_encryption_key(
        gh_repository,
        gh_token,
    )
    encrypted_secrets = {
        k: encrypt_using_key(v, key=encryption_key)
        for k, v in secrets.items()
    }
    for secret_name, secret_value in encrypted_secrets:
        # PUT /repos/:owner/:repo/actions/secrets/:name
        r.put(
            (
                f'https://api.github.com/repos/{gh_repository}/'
                f'actions/secrets/{secret_name}'
            ),
            headers={
                'Authorization': f'token {gh_token}',
            },
            json={
                'key_id': encryption_key_id,
                'encrypted_value': secret_value,
            },
        )


def encrypt_using_key(
        value: str,
        key: str,
) -> str:
    sealed_box = public.SealedBox(
        public.PublicKey(
            key.encode('utf-8'),
            encoding.Base64Encoder(),
        ),
    )
    encrypted = sealed_box.encrypt(value.encode('utf-8'))

    return base64.b64encode(encrypted).decode('utf-8')


def get_encryption_key(
        gh_repo: str,
        gh_token: str,
) -> t.Tuple[str, str]:
    # GET /repos/:owner/:repo/actions/secrets/public-key
    public_key = r.get(
        f'https://api.github.com/repos/{gh_repo}/actions/secrets/public-key',
        headers={
            'Authorization': f'token {gh_token}',
            'Content-Type': 'application/json',
        },
    ).json()
    return public_key['key'], public_key['key_id']


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
