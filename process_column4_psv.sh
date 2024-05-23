#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <psv-file>"
  exit 1
fi

input_file="$1"
output_file="output_${input_file}"

# Process the input file
while IFS= read -r line; do
  # Use cut to extract the 4th column and other columns
  col1=$(echo "$line" | cut -d'|' -f1)
  col2=$(echo "$line" | cut -d'|' -f2)
  col3=$(echo "$line" | cut -d'|' -f3)
  col4=$(echo "$line" | cut -d'|' -f4)
  col5=$(echo "$line" | cut -d'|' -f5-)

  # Use sed to replace xxx.0 with xxx in the 4th column
  col4=$(echo "$col4" | sed 's/^\([0-9]\+\)\.0$/\1/')

  # Reconstruct the line
  new_line="${col1}|${col2}|${col3}|${col4}|${col5}"
  
  # Print the new line to the output file
  echo "$new_line" >> "$output_file"
done < "$input_file"

echo "Processing complete. Output written to $output_file"
