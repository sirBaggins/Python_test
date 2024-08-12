from pygame import font, init, Rect

init()

# CONFIGS
GAME_NAME:str = "RIDDLED"
SCREEN_WIDTH:int = 800
SCREEN_HEIGHT:int = 800
SCREEN_WIDTH_HEIGHT:tuple = (SCREEN_WIDTH, SCREEN_HEIGHT)
FPS:int = 60


# COLOURS
BLACK:tuple = (0, 0, 0)
WHITE:tuple = (255, 255, 255)
DARK_BLUE:tuple = (13, 27, 42)
LAVENDER:tuple = (178, 154, 173)
PURPLE:tuple = (44, 42, 74)
YELLOW:tuple = (224, 212, 102)
GREEN:tuple = (82, 121, 111)
DARK_GREEN:tuple = (28, 79, 63)

BOX_DIALOG:Rect = Rect(0, 650, 800, 150)

# FONTS
FONT_ANNIE_PATH:str = "../graphics/Font/Annie_Use_Your_Telescope/AnnieUseYourTelescope-Regular.ttf"
FONT_MAIN_HUGE:font.Font = font.Font(FONT_ANNIE_PATH, 50)
FONT_MAIN_NORMAL:font.Font = font.Font(FONT_ANNIE_PATH, 40)


# IMAGES
    # BACKGROUNDS
MENU_MAIN_BG:str = "../graphics/Backgrounds/menu_main_background.png"
MAIN_SCENE_BACKGROUND:str = "../graphics/Backgrounds/scene_background.jpg"
    # SPRITE
SPRITE_MAN:str =  "../graphics/Sprites/The_man.png"
SPRITE_CROW:str = "../graphics/Sprites/The_crow.png"
SPRITE_DOG:str = "../graphics/Sprites/The_dog.png"
SPRITE_DRAGON:str = "../graphics/Sprites/The_dragon.png"

SPRITE_SIZE:tuple = (150, 150)

# MUSIC
SONG_AURA_PATH:str = "../audio/bg_music_aura.mp3"

# CONSTANTS
TOPLEFT:tuple = (0, 0)



if __name__ == "__main__":
    print("do not run this file by itself. Run 'main.py'")