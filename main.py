import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set the width and height of each grid cell
WIDTH = 50
HEIGHT = 50

# Set the margin between each grid cell
MARGIN = 5

# Initialize Pygame
pygame.init()

# Set the size of the game window
WINDOW_SIZE = [560, 560]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set the title of the game window
pygame.display.set_caption("Grid Game")

# Create a 2D array of the grid
grid = []
for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0)

# Set the starting position of the token
token_row = 0
token_column = 0

# Set the clock for the game
clock = pygame.time.Clock()


# Set the game loop flag
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if token_column > 0:
                    token_column -= 1
            elif event.key == pygame.K_RIGHT:
                if token_column < 9:
                    token_column += 1
            elif event.key == pygame.K_UP:
                if token_row > 0:
                    token_row -= 1
            elif event.key == pygame.K_DOWN:
                if token_row < 9:
                    token_row += 1

    # Fill the background with white
    screen.fill(WHITE)

    # Draw the grid
    for row in range(10):
        for column in range(10):
            color = BLACK
            if row == token_row and column == token_column:
                color = RED
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN,
                                             (MARGIN + HEIGHT) * row + MARGIN,
                                             WIDTH,
                                             HEIGHT])

    # Update the screen
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()

