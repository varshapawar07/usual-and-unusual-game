game_project/
├── assets/                            # Contains all media assets for the game
│   ├── images/
│   │   ├── characters/                # Character images and sprites
│   │   │   ├── boy/                   # Outfit options for the boy character
│   │   │   └── girl/                  # Outfit options for the girl character
│   │   ├── environments/              # Backgrounds for different game settings (Fun Fair, School, etc.)
│   │   └── ui/                        # UI elements like buttons, icons, etc.
│   ├── sounds/
│   │   ├── voice_guidance/            # Audio files providing voice guidance to players
│   │   └── sfx/                       # Sound effects (e.g., button clicks, level completion sounds)
│   └── fonts/                         # Custom fonts for game text
│
├── src/                               # Contains the main codebase for the game
│   ├── characters/
│   │   ├── character_selection.py     # Code for the character selection screen
│   │   └── character_customization.py # Code for character customization (dressing up characters)
│   ├── levels/
│   │   ├── level1.py                  # Code for Level 1 of each setting (e.g., Fun Fair, School)
│   │   ├── level2.py                  # Code for Level 2, etc.
│   │   └── ...                        # Additional levels for each setting
│   ├── main_menu.py                   # Code for the main options menu, where players choose game settings
│   ├── gameplay.py                    # Core gameplay logic, including safety scenarios
│   ├── rewards.py                     # Manages player rewards and progression between levels
│   └── save_load.py                   # Handles saving and loading player progress
│
├── config/                            # Configuration files for game settings and constants
│   ├── settings.py                    # General game settings and configurations
│   └── constants.py                   # Constants used throughout the game, such as file paths and level names
│
├── game.py                            # Main file to initialize and launch the game
├── README.md                          # Documentation for the game project
└── requirements.txt                   # List of Python dependencies for easy setup


# Child Safety Game Project

This game teaches children about personal safety in various scenarios using an interactive approach. Players can select and dress up a character and progress through levels that educate about safe and unsafe situations.

## Folder Structure
- **assets/**: Contains all media assets for the game.
- **src/**: Holds the game code and logic.
- **config/**: Stores game settings and constants.
- **game.py**: Main file to start the game.

## Getting Started
1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the game:
    ```bash
    python game.py
    ```

Enjoy learning and teaching personal safety in a fun, interactive way!
