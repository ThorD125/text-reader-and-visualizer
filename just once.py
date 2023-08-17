from gtts import gTTS
from io import BytesIO
import pygame

def read_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        for line in lines:
            # Remove '#', '-', and '>' characters
            filtered_line = line.replace('#', '').replace('-', '').replace('>', '')

            if filtered_line.strip():  # Check if there's content to read
                # Print to console
                print(filtered_line)

                # Read out loud in Dutch (language code 'nl')
                tts = gTTS(filtered_line, lang='nl')
                speech_stream = BytesIO()
                tts.write_to_fp(speech_stream)
                speech_stream.seek(0)

                pygame.mixer.init()
                pygame.mixer.music.load(speech_stream)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)

if __name__ == "__main__":
    file_path = "./reads/01 - testfile.md"  # Replace with the actual file path

    print(f"Processing file: {file_path}")
    read_lines(file_path)
    print("\n-----\n")
