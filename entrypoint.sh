#!/usr/bin/env sh

python -m ghsa \
  "${1}" \
  --repo "${2}" \
  --token "${3}"
