import pygame
import Text


class Button:
    def __init__(
        self,
        cords,
        width,
        height,
        funct,
        centered=True,
        text=None,
        font_size=36,
        border=2,
        accent_color=pygame.Color("white"),
        default_color=pygame.Color("chartreuse"),
        clicked_color=pygame.Color("chartreuse3"),
        toggle=False,
    ):
        x, y = cords
        self.centered = centered
        # Checking if the button is centered - if so, the x and y coordinates are at the center
        # Otherwise the x and y coordinates are assumed to be the upper left corner
        if self.centered:
            x -= int(width / 2)
            y -= int(height / 2)
            self.text = Text.Text(text, cords)
        else:
            self.text = Text.Text(text, (x + int(width / 2), y + int(height / 2)))
        self.left_x = x
        self.top_y = y
        self.right_x = x + width
        self.bottom_y = y + height
        self.width = width
        self.height = height
        self.font_size = font_size
        self.border = border
        self.accent_color = accent_color
        self.function = funct
        self.default_color = default_color
        self.clicked_color = clicked_color
        self.toggle = toggle
        self.clicked = False

    def get_text(self):
        return self.text.get_text()

    def change_clicked(self):
        self.clicked = not self.clicked

    def is_clicked(self):
        return self.clicked

    def check_for_click(self, event, mouse_x, mouse_y):
        # Checks for the click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (
                mouse_x > self.left_x
                and mouse_x < self.right_x
                and mouse_y > self.top_y
                and mouse_y < self.bottom_y
            ):
                # If it's a toggle, the function is run now
                if self.toggle:
                    self.function()
                    self.clicked = not self.clicked
                else:
                    self.clicked = True
        # If the button is no longer being clicked and it isn't a toggle, stops the click
        elif event.type == pygame.MOUSEBUTTONUP and self.clicked and not self.toggle:
            self.function()
            self.clicked = False

    def render(self, window):
        # Renders differently depending on if it's being clicked or not
        if self.clicked:
            rect_color = self.clicked_color
        else:
            rect_color = self.default_color
        # Draws the rectangle for the button
        pygame.draw.rect(
            window, rect_color, (self.left_x, self.top_y, self.width, self.height)
        )
        # If the rectangle has a border, draws the border
        if self.border:
            pygame.draw.rect(
                window,
                self.accent_color,
                (self.left_x, self.top_y, self.width, self.height),
                self.border,
            )
        # Renders the button's text (if it has any)
        self.text.render(window)
