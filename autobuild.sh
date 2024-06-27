#!/usr/bin/env bash

set -e

inotifywait -e modify -m chapters etc main.tex |
  while read -r _; do
    npm run fix && npm run build
    notify-send "Thesis auto builder" "New build available"
  done
