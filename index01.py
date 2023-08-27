import pygame
import sys
import time
import os
from gtts import gTTS
from io import BytesIO
import pygame

thelanguage="en"


if 1 < len(sys.argv):
    thelanguage = sys.argv[1]


class TextOnScreen:
    def __init__(self):
        pygame.init()
        self.screen_info = pygame.display.Info()  # Get screen info
        self.width, self.height = self.screen_info.current_w, self.screen_info.current_h
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        pygame.display.set_caption("Text on Pygame Screen")
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.font = pygame.font.Font(None, 144)
        self.current_text = "Hello, Pygame!"
        self.text = self.font.render(self.current_text, True, self.black, self.white)
        self.text_rect = self.text.get_rect(center=(self.width // 2, self.height // 2))

    def change_text(self, new_text):
        self.current_text = new_text
        self.text = self.font.render(self.current_text, True, self.white, self.black)
        self.text_rect = self.text.get_rect(center=(self.width // 2, self.height // 2))

    def update_display(self):
        pygame.event.get()
        self.screen.fill(self.black)
        self.screen.blit(self.text, self.text_rect)
        pygame.display.flip()

    def quit(self):
        pygame.quit()
        sys.exit()

import re

def read_lines_incrementally(game, file_path, max_lines):
    with open(file_path, 'r', encoding='utf-8') as file:  # Specify the encoding
        lines = file.readlines()

        non_empty_lines = [line.strip() for line in lines if line.strip()]

        for content in non_empty_lines:

            # Remove '#', '-', and '>' characters
            filtered_content = content.replace(';', '').replace('<br>', '').replace('|', '').replace('#', '').replace('->', '').replace('-', '').replace('⦁', '').replace('`','').replace('*','').replace('…','')

            if filtered_content.strip():  # Check if there's content to read
                # Print to console

                for line in filtered_content.splitlines():
                    # Remove any leading and trailing spaces
                    fixedLine = re.sub(r"\t", " ", re.sub(r'\s+', " ", line)).strip()

                    print(fixedLine)

                    splits = fixedLine.split(' ')

                    splittext = ""


                    fixedLines = []

                    count = 0
                    for x in splits:
                        count += 1
                        
                        if 0<len(fixedLines):
                            if fixedLines[-1] == splittext:
                                fixedLines.pop()
                        splittext += x + " "
                        fixedLines.append(splittext)
                        if count > 4:
                            count = 0
                            splittext = ""
                    
                    for fixedLine in fixedLines:
                        print(fixedLine)

                        # Display on screen        
                        game.change_text(fixedLine)
                        game.update_display()


                        # Read out loud in Dutch (language code 'nl')
                        try:
                            tts = gTTS(fixedLine, lang=thelanguage)
                            speech_stream = BytesIO()
                            tts.write_to_fp(speech_stream)
                            speech_stream.seek(0)
                            pygame.mixer.init()
                            pygame.mixer.music.load(speech_stream)
                            pygame.mixer.music.play()
                            while pygame.mixer.music.get_busy():
                                pygame.time.Clock().tick(10)
                        except:
                            print("Error")
                            pass

if __name__ == "__main__":
    directory_path = "./cyber"  # Replace with the actual directory path
    file_list = os.listdir(directory_path)

    game = TextOnScreen()
    # game = None

    for filename in file_list:
        if filename.endswith(".md"):
            file_path = os.path.join(directory_path, filename)
            print(f"Processing file: {file_path}")
            read_lines_incrementally(game, file_path, max_lines=5)  # Adjust max_lines as needed
            print("\n-----\n")
    game.quit()
