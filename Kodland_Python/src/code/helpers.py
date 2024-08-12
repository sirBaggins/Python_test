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

        case _:
            raise ValueError("scene doesn't exist.")


def current_scene(scene_counter:int) -> str:
    match scene_counter:
        case 0:
            return "menu"
        
        case _:
            raise ValueError("scene index does not exist.")
        

def text_center(message, colour):
    txt = FONT_MAIN_HUGE.render(message, True, colour)
    txt_rect = txt.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    return txt, txt_rect


if __name__ == "__main__":
    print("do not run this file by itself. Run 'main.py'")