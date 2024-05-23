#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <psv-file> <column-numbers>"
  echo "Example: $0 input.psv 1 4"
  exit 1
fi

input_file="$1"
shift
columns=("$@")
output_file="output_${input_file}"

# Function to strip .0 from a column if present
strip_decimal() {
  echo "$1" | sed 's/^\([0-9]\+\)\.0$/\1/'
}

# Process the input file
while IFS= read -r line; do
  IFS='|' read -ra fields <<< "$line"
  
  for col in "${columns[@]}"; do
    if [[ "$col" -gt 0 && "$col" -le "${#fields[@]}" ]]; then
      fields[$((col-1))]=$(strip_decimal "${fields[$((col-1))]}")
    fi
  done

  new_line=$(IFS='|'; echo "${fields[*]}")
  
  # Print the new line to the output file
  echo "$new_line" >> "$output_file"
done < "$input_file"

echo "Processing complete. Output written to $output_file"
