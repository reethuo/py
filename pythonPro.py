import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Ball Animation")

# Ball properties
ball_radius = 20
ball_x = random.randint(ball_radius, screen_width - ball_radius)
ball_y = random.randint(ball_radius, screen_height - ball_radius)
ball_dx = random.choice([1, -1]) * random.randint(2, 5)
ball_dy = random.choice([1, -1]) * random.randint(2, 5)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set FPS (frames per second)
clock = pygame.time.Clock()

# Game Loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen with a black background
    screen.fill(BLACK)

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Bounce the ball off the walls and change color randomly
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= screen_width:
        ball_dx *= -1
        ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= screen_height:
        ball_dy *= -1
        ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Draw the ball with the new color
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    # Update the display
    pygame.display.flip()

    # Set FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
