import re

def modify_line(line):
    fields = re.findall(r"'([^']*)'", line)  # Extract fields between single quotes
    modified_fields = []

    for field in fields:
        modified_field = ''.join(
            chr(((ord(char) - ord('a') + 4) % 26) + ord('a')) if 'a' <= char <= 'z' else
            chr(((ord(char) - ord('A') + 4) % 26) + ord('A')) if 'A' <= char <= 'Z' else
            char
            for char in reversed(field)
        )
        modified_fields.append(modified_field)

    return "('" + "', '".join(modified_fields) + "')"

def process_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            modified_line = modify_line(line.strip())
            outfile.write(modified_line + '\n')

if __name__ == "__main__":
    input_file_name = 'input.txt'  # Replace with the actual input file name
    output_file_name = 'output.txt'  # Replace with the desired output file name

    process_file(input_file_name, output_file_name)
