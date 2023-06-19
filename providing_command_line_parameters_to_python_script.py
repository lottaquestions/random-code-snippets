import argparse

def read_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        for line1, line2 in zip(f1, f2):
            print(f"File1: {line1.strip()}, File2: {line2.strip()}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Read two files line by line.')
    parser.add_argument('file1', type=str, help='First file to read')
    parser.add_argument('file2', type=str, help='Second file to read')

    args = parser.parse_args()

    read_files(args.file1, args.file2)
