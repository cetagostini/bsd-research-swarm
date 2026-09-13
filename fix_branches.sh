#!/usr/bin/env bash
set -euo pipefail
cd /tmp/bsd-research-swarm
git stash --include-untracked 2>/dev/null || true

for branch in \
  group-a-iwasawa \
  group-b-euler-systems \
  group-c-arithmetic-statistics \
  group-d-tate-shafarevich \
  group-e-padic-methods \
  group-f-motivic-cohomological \
  group-g-deformation-langlands \
  group-h-computational \
  group-i-connections \
  group-j-unconventional
do
  echo "=== Processing $branch ==="
  git checkout "$branch"
  git merge main --no-edit -m "Merge main into $branch: incorporate result files"
  git push origin "$branch"
  echo "=== Done $branch ==="
done

git checkout main
git stash pop 2>/dev/null || true
echo "All branches updated."
