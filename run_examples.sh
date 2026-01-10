#!/usr/bin/env bash

echo "Running Consolide examples"
echo

for dir in examples/*; do
  if [ -d "$dir" ]; then
    echo "=============================="
    echo "Running $(basename "$dir")"
    echo "=============================="
    python "$dir/main.py"
    echo
  fi
done

echo "Done."
