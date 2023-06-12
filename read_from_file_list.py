# import necessary libraries
import re

# define the function that reads the file
def read_file(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data

# define the function that processes the data
def process_data(data):
    # use a regex to split the data into sections
    sections = re.split(r'\n(?=[A-Z])', data)
    # create a list to store the processed data
    data_list = []
    # process each section
    for section in sections:
        # split the section into lines
        lines = section.split('\n')
        # the title of the section is the first line
        title = lines[0]
        # create a list for the key-value pairs in this section
        section_list = []
        # process each line (except the first one)
        for line in lines[1:]:
            # split the line into a key and a value
            key, value = re.match(r'\s*([a-z\-]+) \"(.*)\"', line).groups()
            # add the key-value pair to the section list
            section_list.append([key, value])
        # add the section list to the main list
        data_list.append([title, section_list])
    return data_list

# main function
def main():
    data = read_file('file.txt')
    data_list = process_data(data)
    print(data_list)

# call the main function
if __name__ == "__main__":
    main()
