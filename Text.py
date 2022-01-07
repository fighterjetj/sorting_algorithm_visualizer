import pygame


class Text:
    def __init__(
        self,
        text,
        cords,
        font_name=None,
        font_size=36,
        font_color=pygame.Color("white"),
        italicize=False,
        bold=False,
        underline=False,
        background=None,
        centered=True,
    ):
        # Initializing instance variables
        self.text = text
        self.x, self.y = cords
        self.font_name = font_name
        self.font_size = font_size
        self.font_color = font_color
        self.make_font()
        self.italicized = italicize
        self.bolded = bold
        self.underlined = underline
        self.background = background
        self.centered = centered
        self.font = pygame.font.Font(self.font_name, self.font_size)
        self.font.set_bold(self.bolded)
        self.font.set_italic(self.italicized)
        self.font.set_underline(self.underlined)

    def italicize(self):
        self.italicized = not self.italicized
        self.font.set_italic(self.italicized)

    def bold(self):
        self.bolded = not self.bolded
        self.font.set_italic(self.bolded)

    def underline(self):
        self.underlined = not self.underlined
        self.font.set_italic(self.underlined)

    def get_text(self):
        return self.text

    def change_text(self, text):
        self.text = text

    def make_font(self):
        # Generates a new font object
        self.font = pygame.font.Font(self.font_name, self.font_size)
        self.font.set_bold(self.bold)
        self.font.set_italic(self.italicize)
        self.font.set_underline(self.underline)

    def change_font(self, font):
        # Changes the font
        self.font_name = font
        self.make_font()

    def change_font_size(self, size):
        # Changes the font size
        self.font_size = size
        self.make_font()

    def render(self, window):
        # Checks if there is no text
        if not self.text:
            return False
        self.word = self.font.render(self.text, True, self.font_color, self.background)
        self.width, self.height = pygame.font.Font.size(self.font, self.text)
        if self.centered:
            window.blit(
                self.word, (self.x - int(self.width / 2), self.y - int(self.height / 2))
            )
        else:
            window.blit(self.word, (self.x, self.y))
        # Return outputs depends on whether or not there was text to be rendered
        return True
