import os

folder_path = "./arman"

try:
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            print(f"Contents of '{filename}':")
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line in file:
                        if line.strip():  # Check if the line is not empty after removing whitespace
                            print(line, end='')
                print("-" * 40)  # Separator between files
            except UnicodeDecodeError:
                print(f"Error decoding '{filename}'. Skipping this file.")
except FileNotFoundError:
    print(f"Folder '{folder_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
