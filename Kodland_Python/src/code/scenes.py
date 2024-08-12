import pygame
from settings import *
from helpers import log, text_center
from dialogs import *

class Scenes:
   
    def __init__(self, screen) -> None:
        self.screen = screen
        self.__load_images()
        self.animation_index:int = 0
        self.scene_counter:int = 0
        
    def render(self, scene_name) -> None:
        match scene_name:
            case "menu":
                self.__render_menu()
            
            case "play":
                self.__render_play()

            case "level_one":
                self.__render_level_one()

            case _:
                log("Scene doesn't exist.")
                self.render_menu

    def __load_images(self) -> None:
        self.menu_background = pygame.image.load(MENU_MAIN_BG)
        self.main_scene_background = pygame.image.load(MAIN_SCENE_BACKGROUND)


    ########################################################
    ######################## SCENES ########################
    ########################################################

    def __render_menu(self) -> None:
        self.screen.blit(self.menu_background, TOPLEFT)
        txt, txt_rect = text_center("PRESS SPACE TO START", BLACK)
        self.screen.blit(txt, txt_rect)

    def __render_play(self) -> None:
        self.screen.fill(BLACK)
        txt, txt_rect = text_center(DIALOG_INTRO[self.animation_index], WHITE)
        self.screen.blit(txt, txt_rect)

    def __render_level_one(self) -> None:
        self.screen.blit(self.main_scene_background, (0, -150))


