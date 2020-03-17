#!/usr/bin/env sh

set -ax

echo $@
env | grep -i INPUT_SECRET_

python -m ghsa \
  "${INPUT_GH-SECRETS}" \
  --repo "${INPUT_REPOSITORY:-$GITHUB_REPOSITORY}" \
  --token "${INPUT_TOKEN}"
