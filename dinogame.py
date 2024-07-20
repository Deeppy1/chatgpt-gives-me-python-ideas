import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dino Game")

# Load assets
dino_image = pygame.Surface((50, 50))
dino_image.fill(BLACK)
obstacle_image = pygame.Surface((20, 50))
obstacle_image.fill(GRAY)

# Dinosaur class
class Dinosaur:
    def __init__(self):
        self.image = dino_image
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT - 100
        self.is_jumping = False
        self.jump_velocity = 10
        self.gravity = 1

    def update(self):
        if self.is_jumping:
            self.rect.y -= self.jump_velocity
            self.jump_velocity -= self.gravity
            if self.jump_velocity < -10:
                self.is_jumping = False
                self.jump_velocity = 10
        if self.rect.y >= SCREEN_HEIGHT - 100:
            self.rect.y = SCREEN_HEIGHT - 100

    def draw(self):
        screen.blit(self.image, self.rect)

# Obstacle class
class Obstacle:
    def __init__(self):
        self.image = obstacle_image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = SCREEN_HEIGHT - 100

    def update(self):
        self.rect.x -= 5
        if self.rect.x < -20:
            self.rect.x = SCREEN_WIDTH

    def draw(self):
        screen.blit(self.image, self.rect)

# Game loop
def game_loop():
    clock = pygame.time.Clock()
    dino = Dinosaur()
    obstacles = [Obstacle()]

    score = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not dino.is_jumping:
                    dino.is_jumping = True

        # Update game objects
        dino.update()
        for obstacle in obstacles:
            obstacle.update()
            if dino.rect.colliderect(obstacle.rect):
                running = False

        # Draw everything
        screen.fill(WHITE)
        dino.draw()
        for obstacle in obstacles:
            obstacle.draw()

        # Display the score
        score += 1
        font = pygame.font.SysFont(None, 36)
        text = font.render(f'Score: {score}', True, BLACK)
        screen.blit(text, (10, 10))

        # Refresh the screen
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

# Start the game
game_loop()

