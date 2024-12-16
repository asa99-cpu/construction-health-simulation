import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Create a screen window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Health Effects Simulation')

# Define colors
WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Load cartoon character (as a simple circle for now)
character_radius = 40

# Health bar setup
max_health = 100
current_health = max_health

# Create the clock object to control frame rate
clock = pygame.time.Clock()

# Function to draw the room and materials
def draw_room():
    screen.fill(LIGHT_BLUE)  # Room color
    pygame.draw.rect(screen, (200, 200, 200), (100, 400, 600, 150))  # Concrete floor
    pygame.draw.rect(screen, (150, 150, 150), (300, 150, 200, 100))  # Cement wall
    pygame.draw.rect(screen, (0, 0, 255), (100, 100, 50, 300))  # Window

# Function to draw the character
def draw_character():
    pygame.draw.circle(screen, GREEN, (400, 250), character_radius)  # Draw a simple cartoon character

# Function to simulate health degradation over time
def update_health():
    global current_health
    if current_health > 0:
        # Simulate health loss based on exposure to construction materials
        current_health -= random.randint(1, 3)  # Simulate minor health deterioration
        if current_health < 0:
            current_health = 0

# Function to display health bar
def draw_health_bar():
    pygame.draw.rect(screen, (255, 255, 255), (20, 20, 200, 20))  # Background of health bar
    pygame.draw.rect(screen, RED, (20, 20, 2 * current_health, 20))  # Health bar filling

# Function to show text (e.g., health state)
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Main game loop
running = True
font = pygame.font.SysFont('Arial', 24)

year = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update health every frame
    update_health()

    # Draw room and character
    draw_room()
    draw_character()

    # Draw health bar
    draw_health_bar()

    # Draw health text
    draw_text(f"Health: {current_health}%", font, (255, 255, 255), 230, 20)

    # Draw year text
    draw_text(f"Year: {2024 + year}", font, (255, 255, 255), 350, 50)

    # Simulate the year passing by
    if year < 20:
        draw_text(f"Living in a room with construction materials!", font, RED, 250, 550)

    # Update the screen
    pygame.display.flip()

    # Control the frame rate (simulate passing time)
    time.sleep(1)  # Pause for 1 second (1 year per second in the simulation)
    year += 1

    if year == 20:
        draw_text("Health effects have taken their toll.", font, RED, 250, 550)

    clock.tick(60)  # Set the frame rate to 60 FPS

pygame.quit()
