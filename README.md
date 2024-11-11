game_project/
├── assets/                           
│   ├── images/
│   │   ├── characters/               
│   │   │   ├── boy/                  
│   │   │   └── girl/                  
│   │   ├── environments/             
│   │   └── ui/                       
│   ├── sounds/
│   │   ├── voice_guidance/            
│   │   └── sfx/                      
│   └── fonts/                        
│
├── src/                               
│   ├── characters/
│   │   ├── character_selection.py    
│   │   └── character_customization.py 
│   ├── levels/
│   │   ├── level1.py                  
│   │   ├── level2.py                
│   │   └── ...                        
│   ├── main_menu.py                 
│   ├── gameplay.py                   
│   ├── rewards.py                    
│   └── save_load.py                
│
├── config/                           
│   ├── settings.py                    
│   └── constants.py                  
│
├── game.py                            
├── README.md                         
└── requirements.txt                   

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
