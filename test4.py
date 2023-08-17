import pygame
import sys

# Initialize pygame
pygame.init()

# Get the screen dimensions
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Fullscreen Message")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Load a font with doubled size
font_size = 144  # Double the previous font size
font = pygame.font.Font(None, font_size)

# Define messages
messages = [
    "Hello, this is the initial message!",
    "This is the updated message!",
]

# Initialize message index and render the initial text
current_message_index = 0
text = font.render(messages[current_message_index], True, white)
text_rect = text.get_rect()
text_rect.center = (screen_width // 2, screen_height // 2)

# Set the initial time
start_time = pygame.time.get_ticks()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    # Get the elapsed time in milliseconds
    elapsed_time = pygame.time.get_ticks() - start_time

    # Change the message after 1000 milliseconds (1 second)
    if elapsed_time >= 1000:
        current_message_index += 1
        if current_message_index >= len(messages):
            # If all messages displayed, exit the loop
            running = False
        else:
            text = font.render(messages[current_message_index], True, white)
            start_time = pygame.time.get_ticks()  # Reset the start time

    screen.blit(text, text_rect)
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
