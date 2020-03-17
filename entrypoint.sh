#!/usr/bin/env sh

env | grep -i INPUT_SECRET-

python -m ghsa \
  "${INPUT_GH-SECRETS}" \
  --repo "${INPUT_REPOSITORY:-$GITHUB_REPOSITORY}" \
  --token "${INPUT_TOKEN}"
