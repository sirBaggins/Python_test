import pygame
from settings import *
from helpers import log, text_center

class Scenes:
   
    def __init__(self, screen) -> None:
        self.screen = screen
        self.__load_images()
        
    def render(self, scene_name) -> None:
        match scene_name:
            case "menu":
                self.__render_menu()

            case _:
                log("Scene doesn't exist.")
                self.render_menu

    def __load_images(self) -> None:
        self.menu_background = pygame.image.load(MENU_MAIN_BG)


    ########################################################
    ######################## SCENES ########################
    ########################################################

    def __render_menu(self) -> None:
        self.screen.blit(self.menu_background, TOPLEFT)
        txt, txt_rect = text_center("PRESS SPACE TO START", BLACK)
        self.screen.blit(txt, txt_rect)
