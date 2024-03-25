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
BROWN = (139, 69, 19)

# Define the game area
game_area_width = SCREEN_WIDTH - 50  # Adjust as needed
game_area_height = SCREEN_HEIGHT   # Adjust as needed

# Load road image or create road-like pattern
road_img = pygame.image.load('/home/atif/Desktop/Devops_learning/cargame_python/road.jpg')  # Load road image
road_img = pygame.transform.scale(road_img, (SCREEN_WIDTH-60, SCREEN_HEIGHT))  # Resize road image

# Define the car
car_width = 60
car_height = 100
car_img = pygame.image.load('/home/atif/Desktop/Devops_learning/cargame_python/redcar.jpg')  # Load car image
car_img = pygame.transform.scale(car_img, (car_width, car_height))  # Resize car image
car_x = SCREEN_WIDTH // 2 - car_width // 2
car_y = SCREEN_HEIGHT - car_height - 20
car_speed = 5

 # Define trees
tree_img = pygame.image.load('/home/atif/Desktop/Devops_learning/cargame_python/trees.jpeg')  # Load tree image
tree_img = pygame.transform.scale(tree_img, (50, 50))  # Resize tree image

# Define potholes
pothole_radius = 10
pothole_speed = 5
potholes = []

clock = pygame.time.Clock()

# Initialize score
score = 0

# Load sound effect
pygame.mixer.init()
collision_sound = pygame.mixer.Sound("/home/atif/Desktop/Devops_learning/cargame_python/explosion.mp3")

# Function to create a new pothole
def create_pothole():
    pothole_x = random.randint(pothole_radius, game_area_width - pothole_radius)
    pothole_y = -pothole_radius
    potholes.append(pygame.Rect(pothole_x, pothole_y, pothole_radius * 2, pothole_radius * 2))

# Main game loop
running = True
while running:
    # Draw road background
    screen.blit(road_img, (0, 0))
    
    #screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the car
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 70:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < SCREEN_WIDTH - car_width - 60:
        car_x += car_speed

    # Move potholes
    for pothole in potholes:
        pothole.y += pothole_speed

        # Check collision with car
        if pothole.colliderect(pygame.Rect(car_x, car_y, car_width, car_height)):
            pygame.mixer.Sound.play(collision_sound)
            running = False

        # Remove pothole if it goes off the screen
        if pothole.y > SCREEN_HEIGHT+-60:
            potholes.remove(pothole)
            score += 1

    # Create new potholes randomly
    if random.randint(0, 100) < 5:
        create_pothole()

    # Draw trees
    for y in range(0, SCREEN_HEIGHT, 50):  # Adjust the step size according to your preference
        screen.blit(tree_img, (20, y))  # Left tree
        screen.blit(tree_img, (SCREEN_WIDTH - 60, y))  # Right tree

    

    # Draw the car
    screen.blit(car_img, (car_x, car_y))
    
     # Draw potholes
    for pothole in potholes:
        pygame.draw.circle(screen, BROWN, (pothole.x + pothole_radius, pothole.y + pothole_radius), pothole_radius)

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
