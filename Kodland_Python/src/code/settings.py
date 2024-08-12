from pygame import font, init

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


# FONTS
FONT_ANNIE_PATH:str = "../graphics/Font/Annie_Use_Your_Telescope/AnnieUseYourTelescope-Regular.ttf"
FONT_MAIN_HUGE:font.Font = font.Font(FONT_ANNIE_PATH, 50)


# IMAGES
    # BACKGROUNDS
MENU_MAIN_BG:str = "../graphics/Backgrounds/menu_main_background.png"
    # BUTTONS
BTN_PLAY_0:str = "../graphics/GUI/btn_play_0.png"
BTN_PLAY_1:str = "../graphics/GUI/btn_play_1.png"

# CONSTANTS
TOPLEFT:tuple = (0, 0)



if __name__ == "__main__":
    print("do not run this file by itself. Run 'main.py'")