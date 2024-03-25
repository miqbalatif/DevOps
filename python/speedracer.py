import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("speedracer Game")

# Define colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the car
car_width = 40
car_height = 80
car_x = SCREEN_WIDTH // 2 - car_width // 2
car_y = SCREEN_HEIGHT - car_height - 20
car_speed = 5

# Define wheel size
wheel_size = 10

# Define potholes
pothole_radius = 10
pothole_speed = 5
potholes = []

clock = pygame.time.Clock()

# Initialize score
score = 0

# Load sound effect
#pygame.mixer.init()
#collision_sound = pygame.mixer.Sound("collision.wav")

# Function to create a new pothole
def create_pothole():
    pothole_x = random.randint(pothole_radius, SCREEN_WIDTH - pothole_radius)
    pothole_y = -pothole_radius
    potholes.append(pygame.Rect(pothole_x, pothole_y, pothole_radius * 2, pothole_radius * 2))

# Main game loop
running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the car
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < SCREEN_WIDTH - car_width:
        car_x += car_speed

    # Move potholes
    for pothole in potholes:
        pothole.y += pothole_speed

        # Check collision with car
        if pothole.colliderect(pygame.Rect(car_x, car_y, car_width, car_height)):
            pygame.mixer.Sound.play(collision_sound)
            running = False

        # Remove pothole if it goes off the screen
        if pothole.y > SCREEN_HEIGHT:
            potholes.remove(pothole)
            score += 1

    # Create new potholes randomly
    if random.randint(0, 100) < 5:
        create_pothole()

    # Draw the car
    pygame.draw.rect(screen, GREEN, (car_x, car_y, car_width, car_height))
    # Draw wheels
    pygame.draw.rect(screen, BLACK, (car_x - wheel_size, car_y + car_height, wheel_size, wheel_size))
    pygame.draw.rect(screen, BLACK, (car_x + car_width, car_y + car_height, wheel_size, wheel_size))

    # Draw potholes
    for pothole in potholes:
        pygame.draw.circle(screen, RED, (pothole.x + pothole_radius, pothole.y + pothole_radius), pothole_radius)

    # Draw score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

# Game over screen
screen.fill((255, 255, 255))
font = pygame.font.Font(None, 72)
game_over_text = font.render("Game Over", True, RED)
score_text = font.render(f"Final Score: {score}", True, RED)
screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2 - 50))
screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2 - score_text.get_height() // 2 + 50))
pygame.display.flip()

# Wait for a moment before exiting
pygame.time.wait(3000)

pygame.quit()
