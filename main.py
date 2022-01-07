import pygame
import Text
import Button
import Input
import sorting_visualizer
import random_list_generator
import bubble_sort
import insertion_sort
import merge_sort
import quick_sort


# Function for buttons that don't need to do anything beyond be clicked
def junk_funct():
    pass


# if __name__ == "__main__":
# Tuple storing the sorting algorithms
SORTING_ALGORITHMS = ("Bubble Sort", "Insertion Sort", "Merge Sort", "Quick Sort")
FPS = 120
WIDTH, HEIGHT = 1400, 600
num_items = 100
window = pygame.display.set_mode((WIDTH, HEIGHT))
# Getting the sorters into a dictionary with their corresponding names
sorters = {}
sorters["Bubble Sort"] = bubble_sort.Sorter
sorters["Insertion Sort"] = insertion_sort.Sorter
sorters["Merge Sort"] = merge_sort.Sorter
sorters["Quick Sort"] = quick_sort.Sorter

# List of everything we need to render
to_render = []
# List of everything that takes input
needs_input = []
# Making a list of all the algorithm buttons
algo_buttons = []

num_val_input = None


def gen_ui():
    global algo_buttons, needs_input, to_render, num_val_input
    # All ui is generated down the middle
    buttons_x = int(WIDTH / 2)
    buttons_y = int(HEIGHT / 5)
    y_offset = 60
    ui_width = 200
    ui_height = 40
    for algorithm in SORTING_ALGORITHMS:
        button = Button.Button(
            cords=(buttons_x, buttons_y),
            width=ui_width,
            height=ui_height,
            funct=junk_funct,
            text=algorithm,
            toggle=True,
        )
        buttons_y += y_offset
        algo_buttons.append(button)
        to_render.append(button)
        needs_input.append(button)
    # Automatically selects the first button
    algo_buttons[0].change_clicked()

    # Makes the text to label the input
    label_text = Text.Text("Number of Items:", (buttons_x, buttons_y))
    to_render.append(label_text)
    buttons_y += y_offset / 1.6

    # Makes the input
    num_val_input = Input.Input(
        (buttons_x, buttons_y), ui_width, ui_height, text="100", int_only=True
    )
    to_render.append(num_val_input)
    needs_input.append(num_val_input)
    buttons_y += y_offset
    # Makes the start button
    start_button = Button.Button(
        (buttons_x, buttons_y), ui_width, ui_height, start_sorting, text="Start Sorting"
    )
    to_render.append(start_button)
    needs_input.append(start_button)


# Function for when we are ready to start sorting
def start_sorting():
    global window
    selected_sorters = []
    # If no number/0 is input, nothing happens
    text = num_val_input.get_text()
    if text == "" or text == "0":
        return False
    rand_list = random_list_generator.gen_list(0, HEIGHT, int(text))
    # First figures out what sorters have been selected
    for algo_button in algo_buttons:
        if algo_button.is_clicked():
            rand_list_copy = rand_list[:]
            selected_sorters.append(sorters[algo_button.get_text()](rand_list_copy))
    # If no selected algorithms, returns false
    if len(selected_sorters) == 0:
        return False
    sorting_visualizer.window_maker(window, HEIGHT, WIDTH, selected_sorters, FPS)


# Window Caption
pygame.display.set_caption("Sorting Algorithm Visualizer")
pygame.init()
# Various objects needed for the program to run
clock = pygame.time.Clock()
gen_ui()
# test_text = Text.Text("Test", (100, 100))
# test_button = Button.Button(
#     (200, 200), 100, 40, number_input, centered=False, text="Test", toggle=True
# )
# test_input = Input.Input((300, 300), 100, 40, text="200")
running = True
while running:
    clock.tick(FPS)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        for object in needs_input:
            object.check_for_click(event, mouse_x, mouse_y)
        # test_button.check_for_click(event, mouse_x, mouse_y)
        # curr_val = test_input.check_for_click(event, mouse_x, mouse_y)
    window.fill(pygame.Color("Black"))
    for object in to_render:
        object.render(window)
    # test_text.render(window)
    # test_button.render(window)
    # test_input.render(window)
    pygame.display.update()

pygame.quit()
