import pygame
import numpy as np
import time

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Health Impact Simulation")

# Load images (For now, use simple rectangles or circles to represent the house and the human character)
house_color = (200, 200, 255)
human_color = (100, 150, 255)  # Human character color (can be replaced with an image later)

# Create a simple function to draw the house and human
def draw_house(screen):
    # Draw a simple house (Rectangle)
    pygame.draw.rect(screen, house_color, (100, 100, 600, 400))  # (x, y, width, height)

def draw_human(screen, year):
    # Human is represented as a circle here (can be replaced with a more complex image or animation)
    # As years increase, the human becomes smaller (representing aging/health deterioration)
    size = max(50 - year * 2, 10)  # Size decreases with age
    pygame.draw.circle(screen, human_color, (400, 350), size)

# Main loop to run the simulation
def run_simulation():
    clock = pygame.time.Clock()
    running = True

    # For simplicity, the years will run from 0 to 20 (simulating 20 years)
    for year in range(21):
        screen.fill((255, 255, 255))  # Clear the screen with white color
        draw_house(screen)  # Draw the house
        draw_human(screen, year)  # Draw the human with size decreasing over time (aging effect)
        
        # Add text showing the current year
        font = pygame.font.SysFont(None, 55)
        text = font.render(f"Year: {year}", True, (0, 0, 0))
        screen.blit(text, (350, 20))
        
        # Add text showing the health risk
        health_risk = 0.1 * year  # Just an example of increasing health risk over time
        health_text = font.render(f"Health Risk: {health_risk:.2f}", True, (0, 0, 0))
        screen.blit(health_text, (300, 500))

        pygame.display.update()  # Update the screen
        
        # Delay for animation effect (adjust as needed for smoothness)
        time.sleep(0.5)  # Delay for 0.5 seconds per year
        clock.tick(30)  # Frame rate (30 frames per second)

    pygame.quit()

# Run the simulation
run_simulation()
