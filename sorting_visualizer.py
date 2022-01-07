import pygame
import random_list_generator
import insertion_sort as curr_sorter

# Constants
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
NUM_ITEMS = 100
FPS = 120
WIDTH, HEIGHT = 900, 500
# Creating the window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# Window Caption
pygame.display.set_caption("Sorting Algorithm Visualizer")
curr_ind = 0
rand_array = random_list_generator.gen_list(0, HEIGHT, 100)
POINTER = curr_sorter.Sorter(rand_array)

# Function that draws the rectangles
def draw_rectangles(window, array, highlight, x_range, y_range):
    if len(x_range) != 2 or len(y_range) != 2:
        raise Exception("x_range and y_range must have 2 values")
    # White and red colors
    white = (255, 255, 255)
    red = (255, 0, 0)
    # Sorts the x_range and y_range so that the two values can be in any order
    x_range.sort()
    y_range.sort()
    maximum = max(array)
    # Width and height of the passed area
    width = abs(x_range[1] - x_range[0])
    height = abs(y_range[1] - y_range[0])
    rect_width = int(width / len(array))
    x = x_range[0]
    for index, val in enumerate(array):
        val = array[index]
        # Calculating the scaled height
        rect_height = val / maximum * height
        pygame.draw.rect(
            window,
            white,
            (x, y_range[1] - rect_height, rect_width, rect_height),
            int(rect_width / 4),
        )
        # The highlighting part
        if index in highlight:
            pygame.draw.rect(
                window, red, (x, y_range[1] - rect_height, rect_width, rect_height)
            )
        x += rect_width


# Function for whatever must be done when drawing the display
def draw_window(window, our_array, index):
    window.fill(BLACK)
    draw_rectangles(our_array, index, [0, WIDTH], [0, HEIGHT], WIN)
    pygame.display.update()


def window_maker(window, win_height, win_width, sorters, fps):
    global rand_array, curr_ind
    clock = pygame.time.Clock()
    running = True
    black = (0, 0, 0)
    white = (255, 255, 255)
    print("The random array is: " + str(rand_array))
    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        window.fill(black)
        # If we have four sorters we will be doing a 2 by 2 grid
        if len(sorters) == 4:
            for index, sorter in enumerate(sorters):
                highlight = sorter.next_step()
                curr_array = sorter.get_array()
                draw_rectangles(
                    window,
                    curr_array,
                    highlight,
                    [
                        ((win_width / 2) * (index % 2)),
                        win_width / 2 + ((win_width / 2) * (index % 2)),
                    ],
                    [
                        (win_height / 2) * int(index / 2),
                        (win_height / 2 + (win_height / 2) * int(index / 2)),
                    ],
                )
            # Dividing the screen into four equal parts
            pygame.draw.line(
                window, white, (0, win_height / 2), (win_width, win_height / 2), 6
            )
            pygame.draw.line(
                window, white, (win_width / 2, 0), (win_width / 2, win_height), 6
            )
        else:
            sub_length = win_width / len(sorters)
            for index, sorter in enumerate(sorters):
                highlight = sorter.next_step()
                curr_array = sorter.get_array()
                draw_rectangles(
                    window,
                    curr_array,
                    highlight,
                    [sub_length * index, sub_length * (index + 1)],
                    [0, win_height],
                )
                # Drawing the dividing line
                if index < len(sorters) - 1:
                    pygame.draw.line(
                        window,
                        white,
                        (sub_length * index, 0),
                        (sub_length * index, win_height),
                        6,
                    )
        pygame.display.update()
    # pygame.quit()


if __name__ == "__main__":
    window_maker(WIN, HEIGHT, WIDTH, [POINTER], FPS)
