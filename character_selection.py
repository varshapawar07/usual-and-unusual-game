from ursina import *
from src.characters.character_customization import CharacterCustomization

class CharacterSelection(Entity):
    def __init__(self):
        super().__init__()
        
        # Display title text
        self.title = Text("Choose Your Character", position=(0, 0.4), scale=2, origin=(0, 0), color=color.black)
        
        # Button for selecting Boy character
        self.boy_button = Button(
            text="Boy",
            color=color.cyan,
            scale=(0.3, 0.15),
            position=(-0.3, 0),
            on_click=self.select_boy
        )
        
        # Button for selecting Girl character
        self.girl_button = Button(
            text="Girl",
            color=color.pink,
            scale=(0.3, 0.15),
            position=(0.3, 0),
            on_click=self.select_girl
        )

    def select_boy(self):
        # Load the boy customization screen
        self.disable()  # Hide the selection screen
        self.customization_screen = CharacterCustomization(character="boy")

    def select_girl(self):
        # Load the girl customization screen
        self.disable()  # Hide the selection screen
        self.customization_screen = CharacterCustomization(character="girl")
