# This is a simple pygame script exploring custom fonts and text rendering

# Import libs
import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 480, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Font test")

# Define Colors
BLUE = (30, 100, 200)
YELLOW = (255, 210, 0)

# Locate custom font
script_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.dirname(script_dir)
font_folder = os.path.join(project_dir, "fonts")
font_file = "Jersey10-Regular.ttf"
font_path = os.path.join(font_folder, font_file)

# Load custom font
custom_font = pygame.font.Font(font_path, 36)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLUE)

    # Render text using custom font
    text_surface = custom_font.render("culture for breakfast?", True, YELLOW)

    # Blit the text surface to the screen
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()