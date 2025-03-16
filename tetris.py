import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
GRID_SIZE = 30
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

# Shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]]  # Z
]

SHAPE_COLORS = [CYAN, YELLOW, PURPLE, ORANGE, BLUE, GREEN, RED]

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Initialize grid
grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Initialize variables
current_shape = random.choice(SHAPES)
current_color = random.choice(SHAPE_COLORS)
current_x = GRID_WIDTH // 2 - len(current_shape[0]) // 2
current_y = 0
clock = pygame.time.Clock()
fall_time = 0
fall_speed = 0.5

def draw_grid():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pygame.draw.rect(screen, grid[y][x], (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)
            pygame.draw.rect(screen, WHITE, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

def draw_shape(shape, color, offset_x, offset_y):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, color, ((offset_x + x) * GRID_SIZE, (offset_y + y) * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)
                pygame.draw.rect(screen, WHITE, ((offset_x + x) * GRID_SIZE, (offset_y + y) * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

def check_collision(shape, offset_x, offset_y):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                if x + offset_x < 0 or x + offset_x >= GRID_WIDTH or y + offset_y >= GRID_HEIGHT:
                    return True
                if grid[y + offset_y][x + offset_x] != BLACK:
                    return True
    return False

def merge_shape(shape, color, offset_x, offset_y):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                grid[y + offset_y][x + offset_x] = color

def clear_lines():
    global grid
    new_grid = [row for row in grid if any(cell == BLACK for cell in row)]
    lines_cleared = GRID_HEIGHT - len(new_grid)
    new_grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(lines_cleared)] + new_grid
    grid = new_grid

def rotate_shape(shape):
    return [[shape[y][x] for y in range(len(shape))] for x in range(len(shape[0]) - 1, -1, -1)]

# Main game loop
running = True
while running:
    screen.fill(BLACK)
    fall_time += clock.get_rawtime()
    clock.tick()

    if fall_time / 1000 >= fall_speed:
        fall_time = 0
        current_y += 1
        if check_collision(current_shape, current_x, current_y):
            current_y -= 1
            merge_shape(current_shape, current_color, current_x, current_y)
            clear_lines()
            current_shape = random.choice(SHAPES)
            current_color = random.choice(SHAPE_COLORS)
            current_x = GRID_WIDTH // 2 - len(current_shape[0]) // 2
            current_y = 0
            if check_collision(current_shape, current_x, current_y):
                running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if not check_collision(current_shape, current_x - 1, current_y):
                    current_x -= 1
            if event.key == pygame.K_RIGHT:
                if not check_collision(current_shape, current_x + 1, current_y):
                    current_x += 1
            if event.key == pygame.K_DOWN:
                if not check_collision(current_shape, current_x, current_y + 1):
                    current_y += 1
            if event.key == pygame.K_UP:
                rotated_shape = rotate_shape(current_shape)
                if not check_collision(rotated_shape, current_x, current_y):
                    current_shape = rotated_shape

    draw_grid()
    draw_shape(current_shape, current_color, current_x, current_y)
    pygame.display.update()

pygame.quit()