#!/usr/bin/env sh

echo $@
env

python -m ghsa \
  "${INPUT_GH-SECRETS}" \
  --repo "${INPUT_REPOSITORY:-$GITHUB_REPOSITORY}" \
  --token "${INPUT_TOKEN}"
