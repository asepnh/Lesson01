import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Game settings
GRAVITY = 0.5
FLAP_STRENGTH = -5
PIPE_WIDTH = 70
PIPE_HEIGHT = 500
PIPE_GAP = 200
PIPE_SPEED = 3

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load bird image and scale it down
bird_img = pygame.image.load("bird.png")
bird_img = pygame.transform.scale(bird_img, (50, 35))  # Adjust the size as needed
bird_rect = bird_img.get_rect(center=(100, SCREEN_HEIGHT // 2))

# Initialize variables
bird_y_velocity = 0
pipes = []
score = 0
font = pygame.font.Font(None, 36)

def create_pipe():
    pipe_height = random.randint(150, 450)
    top_pipe = pygame.Rect(SCREEN_WIDTH, pipe_height - PIPE_HEIGHT - PIPE_GAP // 2, PIPE_WIDTH, PIPE_HEIGHT)
    bottom_pipe = pygame.Rect(SCREEN_WIDTH, pipe_height + PIPE_GAP // 2, PIPE_WIDTH, PIPE_HEIGHT)
    return top_pipe, bottom_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= PIPE_SPEED
    return [pipe for pipe in pipes if pipe.right > 0]

def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)

def check_collision(bird_rect, pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return True
    if bird_rect.top <= 0 or bird_rect.bottom >= SCREEN_HEIGHT:
        return True
    return False

def display_score(score):
    score_surface = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_surface, (10, 10))

# Main game loop
running = True
clock = pygame.time.Clock()
pipe_timer = pygame.USEREVENT + 1
pygame.time.set_timer(pipe_timer, 1500)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y_velocity = FLAP_STRENGTH
        if event.type == pipe_timer:
            pipes.extend(create_pipe())

    bird_y_velocity += GRAVITY
    bird_rect.centery += bird_y_velocity

    pipes = move_pipes(pipes)

    screen.fill(WHITE)
    screen.blit(bird_img, bird_rect)
    draw_pipes(pipes)
    display_score(score)

    if check_collision(bird_rect, pipes):
        running = False

    for pipe in pipes:
        if pipe.centerx == bird_rect.centerx:
            score += 1

    pygame.display.update()
    clock.tick(30)

pygame.quit()