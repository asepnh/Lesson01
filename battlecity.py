import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Tank settings
TANK_SIZE = 40
TANK_SPEED = 5
BULLET_SPEED = 10
BULLET_SIZE = 5

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Battle City")

# Initialize clock
clock = pygame.time.Clock()

# Tank class
class Tank:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, TANK_SIZE, TANK_SIZE)
        self.color = color
        self.direction = 'UP'
        self.bullets = []

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def shoot(self):
        if self.direction == 'UP':
            bullet = pygame.Rect(self.rect.centerx, self.rect.top, BULLET_SIZE, BULLET_SIZE)
            self.bullets.append((bullet, (0, -BULLET_SPEED)))
        elif self.direction == 'DOWN':
            bullet = pygame.Rect(self.rect.centerx, self.rect.bottom, BULLET_SIZE, BULLET_SIZE)
            self.bullets.append((bullet, (0, BULLET_SPEED)))
        elif self.direction == 'LEFT':
            bullet = pygame.Rect(self.rect.left, self.rect.centery, BULLET_SIZE, BULLET_SIZE)
            self.bullets.append((bullet, (-BULLET_SPEED, 0)))
        elif self.direction == 'RIGHT':
            bullet = pygame.Rect(self.rect.right, self.rect.centery, BULLET_SIZE, BULLET_SIZE)
            self.bullets.append((bullet, (BULLET_SPEED, 0)))

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        for bullet, _ in self.bullets:
            pygame.draw.rect(screen, RED, bullet)

    def update_bullets(self):
        for bullet, velocity in self.bullets:
            bullet.x += velocity[0]
            bullet.y += velocity[1]
        self.bullets = [b for b in self.bullets if screen.get_rect().colliderect(b[0])]

# Initialize player tank
player_tank = Tank(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, GREEN)

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_tank.shoot()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_tank.move(-TANK_SPEED, 0)
        player_tank.direction = 'LEFT'
    if keys[pygame.K_RIGHT]:
        player_tank.move(TANK_SPEED, 0)
        player_tank.direction = 'RIGHT'
    if keys[pygame.K_UP]:
        player_tank.move(0, -TANK_SPEED)
        player_tank.direction = 'UP'
    if keys[pygame.K_DOWN]:
        player_tank.move(0, TANK_SPEED)
        player_tank.direction = 'DOWN'

    player_tank.update_bullets()
    player_tank.draw(screen)

    pygame.display.update()
    clock.tick(30)

pygame.quit()