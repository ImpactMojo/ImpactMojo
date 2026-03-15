#!/bin/bash
# restore-static-content.sh
#
# Emergency rollback: restores all course HTML files to their original
# static versions (with inline content) from before the dynamic migration.
#
# Usage:
#   bash scripts/restore-static-content.sh
#
# This does NOT undo the migration/edge-function/loader changes — it only
# restores the course HTML files so the site works without the edge function.

set -e

TAG="pre-dynamic-content"
COURSES=(gandhi dataviz devecon mel media law poa devai SEL)

echo "Restoring course HTML files from tag: $TAG"
echo ""

for course in "${COURSES[@]}"; do
    echo "  Restoring courses/$course/index.html"
    git checkout "$TAG" -- "courses/$course/index.html"
done

echo ""
echo "Done. All course files restored to static versions."
echo "You may also want to remove the course-loader.js script tag from each file."
echo ""
echo "To commit the rollback:"
echo "  git add courses/ && git commit -m 'Rollback: restore static course content'"
