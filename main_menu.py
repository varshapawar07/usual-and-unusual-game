from ursina import *

class MainMenu(Entity):
    def __init__(self, start_new_game):
        super().__init__()
        self.start_button = Button(text="Start New Game", color=color.green, scale=(0.3, 0.1), on_click=start_new_game)
        self.start_button.position = (0, 0.2)
        # Add more buttons or functionality as needed
