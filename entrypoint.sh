#!/usr/bin/env sh

python -m ghsa \
  "${INPUT_GH-TOKEN}" \
  --repo "${INPUT_GH-REPOSITORY}" \
  --token "${INPUT_GH-SECRETS}"
