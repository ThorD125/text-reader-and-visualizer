import os

def read_lines_incrementally(file_path, max_lines):
    with open(file_path, 'r') as file:
        lines = file.readlines()

        non_empty_lines = [line.strip() for line in lines if line.strip()]

        for i in range(1, min(len(non_empty_lines), max_lines) + 1):
            print('\n'.join(non_empty_lines[:i]))

if __name__ == "__main__":
    directory_path = "./reads"  # Replace with the actual directory path
    file_list = os.listdir(directory_path)

    for filename in file_list:
        if filename.endswith(".md"):
            file_path = os.path.join(directory_path, filename)
            print(f"Processing file: {file_path}")
            read_lines_incrementally(file_path, max_lines=5)  # Adjust max_lines as needed
            print("\n-----\n")
