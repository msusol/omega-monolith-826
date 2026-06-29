#!/usr/bin/env zsh
set -euo pipefail

PROJECT="omega-monolith-826"

current=$(gcloud config get-value project 2>/dev/null)
if [[ "$current" != "$PROJECT" ]]; then
  gcloud config set project "$PROJECT"
fi

gcloud app deploy app.yaml --quiet
