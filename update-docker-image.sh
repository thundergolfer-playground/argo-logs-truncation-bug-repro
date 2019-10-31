#!/usr/bin/env bash

# Important!: This script requires first that 'docker login' is done.

COMMIT_ID=$(git rev-parse --short=8 HEAD)

docker build -t "argo-logs-truncation-bug-repro:${COMMIT_ID}" .
docker tag "argo-logs-truncation-bug-repro:${COMMIT_ID}" "thundergolfer/argo-logs-truncation-bug-repro:${COMMIT_ID}"

docker push "thundergolfer/argo-logs-truncation-bug-repro:${COMMIT_ID}"

