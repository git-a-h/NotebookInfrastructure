#!/bin/bash

# Find all .coverage files 
files=$(ls -a .*-coverage 2>/dev/null)

if [ -e "$files" ]; then
  echo "No coverage files found."
  exit 1
fi

# Combine the coverage reports
coverage combine $files
coverage html
