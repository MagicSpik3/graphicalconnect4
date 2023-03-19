import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set the width and height of each grid cell
WIDTH = 50
HEIGHT = 50

# Set the offset for the extra row
y_pos_offset = 2 * HEIGHT

# Create the extra column for the selection
y_pre_col = ()

# Define the game board dimensions
my_ROWS = 6
my_COLS = 7


# Set the margin between each grid cell
MARGIN = 5

# Create a font object to draw the numbers

# Initialize Pygame fonts
pygame.font.init()
font_size = 25
font = pygame.font.SysFont(None, font_size)


# Initialize Pygame
pygame.init()

# Set the size of the game window
WINDOW_SIZE = [((my_COLS + 1) * HEIGHT + 25), ((my_ROWS + 3) * WIDTH + 25)]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set the title of the game window
pygame.display.set_caption("Grid Game")

# Set the circle diameter and color
circle_diameter = 50
circle_color = (255, 0, 0)  # Red

# Create a 2D array of the grid
grid = []
for row in range(my_ROWS):
    grid.append([])
    for column in range(my_COLS):
        grid[row].append(0)

# Set the starting position of the token
token_row = 0
token_column = 0

# Set the clock for the game
clock = pygame.time.Clock()

# Give instructions on the game
print("IMPORTANT!")
print("left and right arrow to move, space to drop the token")

# Function to draw the grid
def draw_grid():
    # Fill the background with white
    screen.fill(WHITE)
    # Draw the grid
    for row in range(my_ROWS):
        y_pos = (MARGIN + HEIGHT) * row + MARGIN + y_pos_offset
        x_pos = (MARGIN + WIDTH) * my_COLS + MARGIN
        # Draw the number in the cell
        num_text = font.render(str(row + 1), True, (0, 0, 0))

        num_pos = (x_pos,
                   y_pos)
        screen.blit(num_text, num_pos)

        for column in range(my_COLS):
            x_pos = (MARGIN + WIDTH) * column + MARGIN

            color = BLACK
            pygame.draw.rect(screen, color, [x_pos,
                                             y_pos,
                                             WIDTH,
                                             HEIGHT])


            y_pos_num = (MARGIN + HEIGHT) * my_ROWS + MARGIN + y_pos_offset
            x_pos_num = (MARGIN + WIDTH) * column + MARGIN
            # Draw the number in the cell
            num_text = font.render(str(column + 1), True, (0, 0, 0))

            num_pos = (x_pos_num,
                       y_pos_num)
            screen.blit(num_text, num_pos)



def draw_token_selection(token_column, player_num):
    # draw a white banner across the top
    color = WHITE
    x_pos = (MARGIN)
    y_pos = (MARGIN)
    x_width = (MARGIN + WIDTH) * my_COLS + MARGIN
    pygame.draw.rect(screen, color, [x_pos,
                                     y_pos,
                                     x_width,
                                     HEIGHT])

    y_pos = (MARGIN + HEIGHT) * 0 + MARGIN
    x_pos = (MARGIN + WIDTH) * token_column + MARGIN
    circle_pos = (x_pos + (WIDTH / 2), y_pos + (HEIGHT / 2))
    pygame.draw.circle(screen, RED, circle_pos, circle_diameter // 2)


def drop_token(token_column, symbol):
    landing_row = my_ROWS
    # Whop the token down the column
    for the_r in range(my_ROWS-1, -1, -1):
        if grid[the_r][token_column] == "0":
            landing_row = the_r
            #print("debug")
            break
    # Now loop for the animation:
    y_pos = (MARGIN + HEIGHT) * landing_row + MARGIN
    x_pos = (MARGIN + WIDTH) * token_column + MARGIN
    circle_pos = (x_pos + (WIDTH / 2), y_pos + (HEIGHT / 2))
    pygame.draw.circle(screen, RED, circle_pos, circle_diameter // 2)




# Set the game loop flag
done = False
while not done:
    draw_grid()
    selected = False
    while not selected:
        draw_token_selection(token_column, 1)
        # This selects the col to drop in
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if token_column > 0:
                        token_column -= 1
                elif event.key == pygame.K_RIGHT:
                    if token_column < my_COLS - 1:
                        token_column += 1
                elif event.key == pygame.K_SPACE:
                    drop_token(token_column, 1)


        # Update the screen
        pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
