import os
from gtts import gTTS
from io import BytesIO
import pygame

def read_lines_incrementally(file_path, max_lines):
    with open(file_path, 'r', encoding='utf-8') as file:  # Specify the encoding
        lines = file.readlines()

        non_empty_lines = [line.strip() for line in lines if line.strip()]

        for i in range(1, min(len(non_empty_lines), max_lines) + 1):
            content = '\n'.join(non_empty_lines[:i])

            # Remove '#', '-', and '>' characters
            filtered_content = content.replace('#', '').replace('-', '').replace('>', '').replace('⦁', '')

            if filtered_content.strip():  # Check if there's content to read
                # Print to console
                print(filtered_content)

                # Read out loud in Dutch (language code 'nl')
                tts = gTTS(filtered_content, lang='nl')
                speech_stream = BytesIO()
                tts.write_to_fp(speech_stream)
                speech_stream.seek(0)

                pygame.mixer.init()
                pygame.mixer.music.load(speech_stream)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)

if __name__ == "__main__":
    directory_path = "./testexam"  # Replace with the actual directory path
    file_list = os.listdir(directory_path)

    for filename in file_list:
        if filename.endswith(".md"):
            file_path = os.path.join(directory_path, filename)
            print(f"Processing file: {file_path}")
            read_lines_incrementally(file_path, max_lines=5)  # Adjust max_lines as needed
            print("\n-----\n")
