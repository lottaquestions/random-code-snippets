def reverse_first_last_fields(line):
    fields = line.strip().split(', ')

    if len(fields) >= 2:
        fields[0] = fields[0][::-1]  # Reverse the first field
        fields[-1] = fields[-1][::-1]  # Reverse the last field

    return ', '.join(fields)

def process_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            modified_line = reverse_first_last_fields(line)
            outfile.write(modified_line + '\n')

if __name__ == "__main__":
    input_file_name = 'input.txt'  # Replace with the actual input file name
    output_file_name = 'output.txt'  # Replace with the desired output file name

    process_file(input_file_name, output_file_name)
