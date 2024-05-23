#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <psv-file>"
  exit 1
fi

input_file="$1"
output_file="output_${input_file}"

# Function to strip .0 from a column if present
strip_decimal() {
  echo "$1" | sed 's/^\([0-9]\+\)\.0$/\1/'
}

# Process the input file
while IFS= read -r line; do
  # Use cut to extract columns
  col1=$(echo "$line" | cut -d'|' -f1)
  col2=$(echo "$line" | cut -d'|' -f2)
  col3=$(echo "$line" | cut -d'|' -f3)
  col4=$(echo "$line" | cut -d'|' -f4)
  rest=$(echo "$line" | cut -d'|' -f5-)

  # Use the strip_decimal function to process the 1st, 2nd, 3rd, and 4th columns
  col1=$(strip_decimal "$col1")
  col2=$(strip_decimal "$col2")
  col3=$(strip_decimal "$col3")
  col4=$(strip_decimal "$col4")

  # Reconstruct the line
  new_line="${col1}|${col2}|${col3}|${col4}|${rest}"
  
  # Print the new line to the output file
  echo "$new_line" >> "$output_file"
done < "$input_file"

echo "Processing complete. Output written to $output_file"
