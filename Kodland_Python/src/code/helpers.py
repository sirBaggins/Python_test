import pygame
from settings import *

def log(message) -> None:
    print(message)
    return


def set_scene(name) -> int:
    match name:
        case "menu":
            return 0
        
        case "play":
            return 1
        
        case "level_one":
            return 2
        
        case "level_two":
            return 3
        
        case "level_crow":
            return 4
        
        case "level_crow1":
            return 5
        
        case "level_crow2":
            return 6
        
        case "crow_end":
            return 7

        case "level_dog":
            return 8
        
        case "level_dog1":
            return 9
        
        case "level_dog2":
            return 10
        
        case "dog_end":
            return 11
        
        case "level_dragon":
            return 12
        
        case "level_dragon1":
            return 13

        case "level_dragon2":
            return 14

        case "dragon_end":
            return 15
        
        case "end_game":
            return 16

        case _:
            raise ValueError("scene doesn't exist.")


def current_scene(scene_counter:int) -> str:
    match scene_counter:
        case 0:
            return "menu"
        
        case 1:
            return "play"
        
        case 2:
            return "level_one"
        
        case 3:
            return "level_two"
        
        case 4:
            return "level_crow"
        
        case 5:
            return "level_crow1"
        
        case 6:
            return "level_crow2"
        
        case 7:
            return "crow_end"
        
        case 8:
            return "level_dog"
        
        case 9:
            return "level_dog1"
        
        case 10:
            return "level_dog2"
        
        case 11:
            return "dog_end"
        
        case 12:
            return "level_dragon"
        
        case 13:
            return "level_dragon1"
        
        case 14:
            return "level_dragon2"
        
        case 15:
            return "dragon_end"
        
        case 16:
            return "end_game"
        
        case _:
            raise ValueError("scene index does not exist.")
        

def text_center(message, colour):
    txt = FONT_MAIN_HUGE.render(message, True, colour)
    txt_rect = txt.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    return txt, txt_rect

def text_bottom(message, colour):
    txt = FONT_MAIN_HUGE.render(message, True, colour)
    txt_rect = txt.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT-75))
    return txt, txt_rect


def play_song(path) -> None:
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()

    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)




if __name__ == "__main__":
    print("do not run this file by itself. Run 'main.py'")