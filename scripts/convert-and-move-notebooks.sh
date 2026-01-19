#!/bin/bash

# This script finds all notebook*.py files, converts them to notebooks and moves them to the a (new) notebooks directory

# Create notebooks directory if it doesn't exist
project_root=$(pwd)
output_dir="$project_root/notebooks"
if [ ! -d "$output_dir" ]; then
    mkdir "$output_dir"
fi

# Find all notebook*.py files, convert them to notebooks and move them to notebooks directory
find "$project_root/src" -type f -name "notebook*.py" | while read file; do
    # convert notebooks
    mpirun --stdin none -np 2 jupytext --to ipynb --execute "$file"
    # move to notebooks directory
    mv "${file%.py}.ipynb" "$output_dir"  
done