import pygame
import Text
import Button


class Input(Button.Button):
    def __init__(
        self,
        cords,
        width,
        height,
        centered=True,
        text="",
        font_size=36,
        border=2,
        accent_color=pygame.Color("white"),
        default_color=pygame.Color("chartreuse"),
        clicked_color=pygame.Color("chartreuse3"),
        int_only=False,
    ):
        # Junk function because inputs are treated as buttons that do nothing for rendering purposes
        def junk_funct():
            pass

        super().__init__(
            cords,
            width,
            height,
            junk_funct,
            centered,
            text,
            font_size,
            border,
            accent_color,
            default_color,
            clicked_color,
            True,
        )
        self.int_only = int_only
        # Though the move cursor function only changes the value, it can be changed if you want to
        # This is because cursor behavior was hard to nail down, so we can change the implementation if needed
        self.move_cursor(len(text))

    def move_cursor(self, new_index):
        self.cursor_ind = new_index

    def check_for_click(self, event, mouse_x, mouse_y):
        # If the input is already selected and you click anywhere, it becomes unselected
        if event.type == pygame.MOUSEBUTTONDOWN and self.clicked:
            self.clicked = False
        # Does the normal checking for a click that a button does,
        super().check_for_click(event, mouse_x, mouse_y)
        # Checks for key presses
        if event.type == pygame.KEYDOWN and self.clicked:
            # Gets the current text in the input
            curr_text = self.text.get_text()
            # You can press return to leave the text box
            if event.key == pygame.K_RETURN:
                self.clicked = False
            # Deletes the letter behind the cursor, then moves the cursor back one
            # Only if we aren't at the beginning with nothing to delete
            elif event.key == pygame.K_BACKSPACE and self.cursor_ind > 0:
                self.text.change_text(
                    curr_text[: self.cursor_ind - 1] + curr_text[self.cursor_ind :]
                )
                self.move_cursor(self.cursor_ind - 1)
            # Pressing up moves you to the beginning
            elif event.key == pygame.K_UP:
                self.move_cursor(0)
            # Pressing down moves you to the end
            elif event.key == pygame.K_DOWN:
                self.move_cursor(len(self.text.get_text()))
            # If you aren't at the beginning, moves you to the left
            elif event.key == pygame.K_LEFT and self.cursor_ind > 0:
                self.move_cursor(self.cursor_ind - 1)
            # If you aren't at the end, moves you to the right
            elif event.key == pygame.K_RIGHT and self.cursor_ind < len(
                self.text.get_text()
            ):
                self.move_cursor(self.cursor_ind + 1)
            # Makes sure the key was printable and then adds it to the text if it isn't integers only
            # If it is integers only, makes sure it is a digit
            elif (not self.int_only and event.unicode.isprintable()) or (
                self.int_only and event.unicode.isdigit()
            ):
                self.move_cursor(self.cursor_ind + 1)
                self.text.change_text(
                    curr_text[: self.cursor_ind]
                    + event.unicode
                    + curr_text[self.cursor_ind :]
                )

    def render(self, window):
        # Renders the button like normal, however to render the cursor we add a | character
        curr_text = self.text.get_text()
        self.text.change_text(
            curr_text[: self.cursor_ind] + "|" + curr_text[self.cursor_ind :]
        )
        super().render(window)
        # After the render is done, we delete the cursor
        self.text.change_text(curr_text)
