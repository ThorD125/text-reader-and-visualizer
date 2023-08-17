import pygame
import sys
import time

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
        self.screen.fill(self.black)
        self.screen.blit(self.text, self.text_rect)
        pygame.display.flip()

    def quit(self):
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = TextOnScreen()

    messages = [
        "Message 1",
        "Message 2",
        "Message 3",
        "Message 4",
        "Message 5"
    ]

    for message in messages:
        game.change_text(message)
        game.update_display()
        pygame.time.wait(1000)  # Wait for 1 second

    game.quit()
