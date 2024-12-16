import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Man Living in a Room for 20 Years')

# Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define clock for controlling frame rate
clock = pygame.time.Clock()

# Man's initial position
x, y = 375, 250
dx, dy = 5, 0  # Movement direction

# Main game loop
running = True
years = 0  # Track the number of years in the simulation

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with white color
    screen.fill(WHITE)

    # Simulate the man moving around the room
    pygame.draw.rect(screen, BLACK, (x, y, 50, 100))  # Drawing the man as a rectangle

    # Update position of the man (move by dx and dy)
    x += dx
    if x > 750 or x < 0:
        dx = -dx  # Change direction if it hits the screen edges

    # Increment years every 100 frames (for simplicity, adjust as needed)
    if pygame.time.get_ticks() % 100 == 0:  # Simulate 1 year per 100 frames
        years += 1
        print(f'Year {years}: The man has lived in the house for {years} years.')

    # Update the display
    pygame.display.flip()

    # Control the frame rate (60 FPS)
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
