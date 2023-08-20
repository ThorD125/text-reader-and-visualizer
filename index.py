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

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                print("Mouse clicked on the screen.")
    
    def quit(self):
        pygame.quit()
        sys.exit()

def read_lines_incrementally(game, file_path, max_lines):
    with open(file_path, 'r', encoding='utf-8') as file:  # Specify the encoding
        lines = file.readlines()

        non_empty_lines = [line.strip() for line in lines if line.strip()]

        for i in range(1, min(len(non_empty_lines), max_lines) + 1):
            content = '\n'.join(non_empty_lines[:i])

            # Remove '#', '-', and '>' characters
            filtered_content = content.replace('<br>', '').replace('#', '').replace('->', '').replace('-', '').replace('⦁', '').replace('`','').replace('*','')

            if filtered_content.strip():  # Check if there's content to read
                # Print to console
                print(filtered_content)

                for line in filtered_content.splitlines():
                    # Remove any leading and trailing spaces
                    fixedLine = line.strip()


                    # Display on screen        
                    game.change_text(fixedLine)
                    game.update_display()


                    # # Read out loud in Dutch (language code 'nl')
                    # tts = gTTS(fixedLine, lang=thelanguage)
                    # speech_stream = BytesIO()
                    # tts.write_to_fp(speech_stream)
                    # speech_stream.seek(0)
                    # pygame.mixer.init()
                    # pygame.mixer.music.load(speech_stream)
                    # pygame.mixer.music.play()
                    # while pygame.mixer.music.get_busy():
                    #     pygame.time.Clock().tick(10)

if __name__ == "__main__":
    directory_path = "./OSC"  # Replace with the actual directory path
    file_list = os.listdir(directory_path)

    # game = None
    game = TextOnScreen()

    for filename in file_list:
        if filename.endswith(".md"):
            file_path = os.path.join(directory_path, filename)
            print(f"Processing file: {file_path}")
            read_lines_incrementally(game, file_path, max_lines=5)  # Adjust max_lines as needed
            print("\n-----\n")
    game.quit()
