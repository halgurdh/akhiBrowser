#!/usr/bin/env bash
# Mails the user through the license server's POST /ops/notify. Never fails the job: the GitHub issue stays the fallback.
# Usage: notify.sh <subject> [file with the text]; needs AKHI_OPS_TOKEN, else it only says it skipped.

subject="$1"
text="${2:+$(cat "$2" 2>/dev/null)}"
text="${text:-$subject}"
text="$text

$GITHUB_SERVER_URL/$GITHUB_REPOSITORY/actions/runs/$GITHUB_RUN_ID"
if [ -z "$AKHI_OPS_TOKEN" ]; then
  echo "No AKHI_OPS_TOKEN, not mailed: $subject"
  exit 0
fi
jq -n --arg subject "$subject" --arg text "$text" '{subject: $subject, text: $text}' |
  curl -fsS -m 30 -X POST "${AKHI_OPS_URL:-https://akhi-license.akhibrowser.workers.dev}/ops/notify" \
    -H "Authorization: Bearer $AKHI_OPS_TOKEN" -H "Content-Type: application/json" --data-binary @- > /dev/null ||
  echo "The mail didn't go out: $subject"
exit 0
