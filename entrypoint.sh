#!/usr/bin/env sh

env | grep -i INPUT

python -m ghsa \
  "${INPUT_GH-SECRETS}" \
  --repo "${INPUT_GH-REPOSITORY:-$GITHUB_REPOSITORY}" \
  --token "${INPUT_GH-TOKEN}"
