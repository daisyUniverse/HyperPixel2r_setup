# This is a simple pygame script exploring animated sprites

# Import libs
import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 480, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Animated Sprites Example")

# Load images for animation
sprite_images = []
for i in range(000, 186):
    formatted_i = "{:03d}".format(i) # hack to get leading zeros in i (cfr. img names)
    image_path = os.path.join("img\\animation", f"frame_{formatted_i}_delay-0.04s.gif")
    image = pygame.image.load(image_path).convert_alpha()
    sprite_images.append(image)

# Get the dimensions of the sprite image
sprite_width = sprite_images[0].get_width()
sprite_height = sprite_images[0].get_height()

# Define Colors
BROWN = (101, 32, 32)
YELLOW = (255, 210, 0)

# Set up clock
clock = pygame.time.Clock()

# Game loop
frame = 0

# set frame rate (FPS)
frame_rate = 60

# center sprite
sprite_x, sprite_y = (WIDTH//2-sprite_width//2),(HEIGHT//2-sprite_height//2)

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BROWN)

    # Draw the current frame of the animation
    screen.blit(sprite_images[frame], (sprite_x, sprite_y))

    # Update the frame
    frame += 1
    if frame >= len(sprite_images):
        frame = 0 

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(frame_rate)

# Quit Pygame
pygame.quit()
sys.exit()