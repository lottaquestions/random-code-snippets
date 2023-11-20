import re
import random

def modify_line(line, field_orders):
    fields = re.findall(r"'([^']*)'", line)  # Extract fields between single quotes
    modified_fields = []

    for field in fields:
        if any(char.isalpha() for char in field):  # Check if the field contains alphabetical characters
            if field not in field_orders:
                # Generate a random order for the field and store it for consistency
                field_orders[field] = random.sample(field, len(field))
            modified_field = ''.join(field_orders[field])
        else:
            modified_field = field
        modified_fields.append(modified_field)

    return "('" + "', '".join(modified_fields) + "')"

def process_file(input_file, output_file):
    field_orders = {}
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            modified_line = modify_line(line.strip(), field_orders)
            outfile.write(modified_line + '\n')

if __name__ == "__main__":
    input_file_name = 'input.txt'  # Replace with the actual input file name
    output_file_name = 'output.txt'  # Replace with the desired output file name

    process_file(input_file_name, output_file_name)
