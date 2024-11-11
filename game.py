from ursina import *

app = Ursina()

class SafetyGame:
    def __init__(self):
        window.title = "Child Safety Game"
        window.color = color.black

        # Set up the main background
        self.background = Entity(
            parent=camera.ui,
            model='quad',
            texture=r'D:\Game_Miniproject\Assets\images\environments\back_2_image.jpg',
            scale=(2, 1),
            position=(0, 0, 1)
        )

        # Start Game Button
        self.start_button = Button(
            text="Start Game",
            color=color.azure,
            scale=(0.4, 0.15),
            position=(0, 0),
            text_color=color.white,
            on_click=self.start_game_with_blink
        )

        self.start_button.border_color = color.dark_gray
        self.start_button.border_width = 0.02
        self.start_button.on_hover = self.on_hover
        self.start_button.on_leave = self.on_leave

        # Variables to hold entities
        self.character_background = None
        self.boy_image = None
        self.girl_image = None
        self.selection_text = None
        self.character_image = None
        self.clothing_options = []
        self.shoe_options = []
        self.place_options = []

    def on_hover(self):
        self.start_button.color = color.lime
        self.start_button.scale = (0.45, 0.18)

    def on_leave(self):
        self.start_button.color = color.azure
        self.start_button.scale = (0.4, 0.15)

    def start_game_with_blink(self):
        self.start_button.animate_scale((0.45, 0.18), duration=0.1)
        invoke(self.reset_button_scale, delay=0.1)
        invoke(self.show_character_selection, delay=0.2)

    def reset_button_scale(self):
        self.start_button.scale = (0.4, 0.15)

    def show_character_selection(self):
        self.start_button.disable()
        self.background.disable()

        self.character_background = Entity(
            parent=camera.ui,
            model='quad',
            texture=r'D:\Game_Miniproject\Assets\images\environments\back_2_image.jpg',
            scale=(2, 1),
            position=(0, 0, 1.5)
        )

        self.selection_text = Text(
            text="Choose Your Character",
            position=(0.1, 0.4),
            scale=2.5,
            color=color.black,
            parent=camera.ui,
            z=-1
        )

        self.boy_image = Button(
            parent=camera.ui,
            model='quad',
            texture=r'D:\Game_Miniproject\Assets\images\characters\boy\boy-1.png',
            scale=(0.5, 0.8),
            position=(-0.4, -0.2),
            color=color.white,
            on_click=lambda: self.select_character("boy"),
            z=-1
        )

        self.girl_image = Button(
            parent=camera.ui,
            model='quad',
            texture=r'D:\Game_Miniproject\Assets\images\characters\girl\girl1.png',
            scale=(0.5, 0.8),
            position=(0.6, -0.2),
            color=color.white,
            on_click=lambda: self.select_character("girl"),
            z=-1
        )

    def select_character(self, character_type):
        print(f"Selected character: {character_type}")
        self.boy_image.disable()
        self.girl_image.disable()
        self.selection_text.disable()
        self.character_background.disable()
        self.show_dressing_screen(character_type)

    def show_dressing_screen(self, character_type):
        self.dressing_background = Entity(
            parent=camera.ui,
            model='quad',
            texture=r'D:\Game_Miniproject\Assets\images\environments\back3.jpg',
            scale=(2, 1),
            position=(0, 0, 1)
        )

        self.character_image = Entity(
            parent=camera.ui,
            model='quad',
            texture=f'D:\\Game_Miniproject\\Assets\\images\\characters\\{character_type}\\{character_type}1.png',
            scale=(0.5, 0.8),
            position=(0, 0)
        )

        # Clothing options
        clothing_textures = [
            r'D:\Game_Miniproject\Assets\images\cloths\girl-cloths\cloth1.jpg',
            r'D:\Game_Miniproject\Assets\images\cloths\girl-cloths\cloth2.jpg',
            r'D:\Game_Miniproject\Assets\images\cloths\girl-cloths\cloth3.jpg',
            r'D:\Game_Miniproject\Assets\images\cloths\girl-cloths\cloth4.jpg',
            r'D:\Game_Miniproject\Assets\images\cloths\girl-cloths\cloth5.jpg',
            r'D:\Game_Miniproject\Assets\images\cloths\girl-cloths\cloth6.jpg'
        ]

        for i, texture in enumerate(clothing_textures):
            button = Button(
                parent=camera.ui,
                model='quad',
                texture=texture,
                scale=(0.2, 0.2),
                position=(-0.7, 0.45 - i * 0.18),
                color=color.white,
                on_click=lambda t=texture: None
            )
            self.clothing_options.append(button)

        # Shoe options (only for girl)
        if character_type == "girl":
            shoe_textures = [
                r'D:\Game_Miniproject\Assets\images\shoes\girlshooes\shoes1.png',
                r'D:\Game_Miniproject\Assets\images\shoes\girlshooes\shoes2.png',
                r'D:\Game_Miniproject\Assets\images\shoes\girlshooes\shoes3.png',
                r'D:\Game_Miniproject\Assets\images\shoes\girlshooes\shoes4.png',
                r'D:\Game_Miniproject\Assets\images\shoes\girlshooes\shoes5.png',
                r'D:\Game_Miniproject\Assets\images\shoes\girlshooes\shoes6.png'
            ]

            for i, texture in enumerate(shoe_textures):
                button = Button(
                    parent=camera.ui,
                    model='quad',
                    texture=texture,
                    scale=(0.2, 0.2),
                    position=(0.7, 0.45 - i * 0.18),
                    color=color.white,
                    on_click=lambda t=texture: None
                )
                self.shoe_options.append(button)

        # Start Game Button
        self.start_game_button = Button(
            text="Start Game",
            color=color.orange,
            scale=(0.25, 0.1),
            position=(0, -0.4),
            text_color=color.white,
            on_click=self.show_place_selection,
            z=-1
        )

    def show_place_selection(self):
        # Disable previous options
        for button in self.clothing_options + self.shoe_options:
            button.disable()

        self.dressing_background.disable()
        self.character_image.disable()
        self.start_game_button.disable()

        # Background for place selection
        self.place_selection_background = Entity(
            parent=camera.ui,
            model='quad',
            texture=r'D:\Game_Miniproject\Assets\images\environments\back2.jpg',
            scale=(2, 1),
            position=(0, 0, 1)
        )

        # Place options
        place_textures = [
            'school.png', 'playground.png', 'carnival.png', 'home.png',
            'mall.png', 'beach.png', 'library.png', 'zoo.png', 'hospital.png'
        ]

        for i, texture in enumerate(place_textures):
            button = Button(
                parent=camera.ui,
                model='quad',
                texture=f'D:\\Game_Miniproject\\Assets\\images\\places\\{texture}',
                scale=(0.3, 0.3),
                position=(i % 3 * 0.4 - 0.4, 0.35 - (i // 3) * 0.3),
                color=color.white,
                on_click=lambda t=texture: self.start_place_game(t)
            )
            self.place_options.append(button)

    def start_place_game(self, place):
        print(f"Starting game in: {place}")

# Run the game
game = SafetyGame()
app.run()
