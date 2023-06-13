def file_reader(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        for line1, line2 in zip(f1, f2):
            yield (line1.strip(), line2.strip())

##### Do this ####
# Use the generator
for lines in file_reader('file1.txt', 'file2.txt'):
    print(lines)

##### Or this ####
# Create the generator
gen = file_reader('file1.txt', 'file2.txt')

# Use the generator
try:
    while True:
        print(next(gen))
except StopIteration:
    print("All lines have been read.")
