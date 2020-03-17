#!/usr/bin/env sh

python -m ghsa \
  "${INPUT_SECRETS}" \
  --repo "${INPUT_REPOSITORY:-$GITHUB_REPOSITORY}" \
  --token "${INPUT_TOKEN}"
