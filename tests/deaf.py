# This is a simple pygame script exploring animated sprites

# Import libs
import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 480, 480
spritesize = 570
hoffset = 22
voffset = 5
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Animated Sprites Example")

# Locate sprite folder
script_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.dirname(script_dir)
sprite_folder = os.path.join(project_dir, "img/deaf_bmp")
frames = len(next(os.walk(sprite_folder))[2])
print(frames)

# Load images for animation
sprite_images = []
for i in range(000, frames):
    formatted_i = "{:03d}".format(i) # hack to get leading zeros in i (cfr. img names)
    print(f"\r[ LOADING FRAME {formatted_i}/{frames} ]", end='')
    image_path = os.path.join(sprite_folder, f"frame_{formatted_i}.bmp")
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (spritesize, spritesize))
    sprite_images.append(image)

# Get the dimensions of the sprite image
sprite_width = spritesize
sprite_height = spritesize

# Define Colors
BROWN = (101, 32, 32)

# Set up clock
clock = pygame.time.Clock()

# Game loop
frame = 0

# set frame rate (FPS)
frame_rate = 30

# center sprite
sprite_x, sprite_y = (WIDTH//2-sprite_width//2+hoffset),(HEIGHT//2-sprite_height//2+voffset)

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
