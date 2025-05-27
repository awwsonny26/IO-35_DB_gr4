#!/usr/bin/env bash
set -euo pipefail

REPO="git@github-awwsonny:awwsonny26/IO-35_DB_gr4.git"
BUILD_DIR="docs/.vitepress/dist"

npm run docs:build

cd "$BUILD_DIR"

git init
git branch -M main
git add -A
git commit -m "deploy: $(date '+%Y-%m-%d %H:%M:%S')"

git push -f "$REPO" main:gh-pages

cd -

