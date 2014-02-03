#!/usr/bin/env bash

# See if git is available. If not, bail.
if ! which git >/dev/null 2>&1; then
  echo "You don't have git installed. You're probably going to want that."
  exit 1
fi

# pwd is the generated directory.

git init > /dev/null

echo "Everything is ready, run 'cd $(basename $(pwd))' and get hacking!"



