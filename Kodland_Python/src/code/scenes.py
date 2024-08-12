import pygame
from settings import *
from helpers import *
from dialogs import *

class Scenes:
   
    def __init__(self, screen) -> None:
        self.screen = screen
        self.__load_images()
        self.animation_index:int = 0
        self.scene_counter:int = 0 ##### MUST BE SET TO 0
        self.level_status:bool = False
        self.answer_buffer:str = ""
        self.riddle:Riddle = Riddle(screen, self.answer_buffer)
        
    def render(self, scene_name) -> None:
        match scene_name:
            case "menu":
                self.__render_menu()
            
            case "play":
                self.__render_play()

            case "level_one":
                self.__render_level_one()

            case "level_two":
                self.__render_level_two()

            case "level_crow":
                self.__render_level_crow()

            case "level_crow1":
                self.__render_level_crow1()

            case "level_crow2":
                self.__render_level_crow2()

            case "crow_end":
                self.__render_crow_end()

            case "level_dog":
                self.__render_level_dog()
            
            case "level_dog1":
                self.__render_level_dog1()

            case "level_dog2":
                self.__render_level_dog2()

            case "dog_end":
                self.__render_dog_end()

            case "level_dragon":
                self.__render_level_dragon()
            
            case "level_dragon1":
                self.__render_level_dragon1()

            case "level_dragon2":
                self.__render_level_dragon2()

            case "dragon_end":
                self.__render_dragon_end()

            case "end_game":
                self.__render_end_game()

            case _:
                log("Scene doesn't exist.")
                self.__render_menu()

    def __load_images(self) -> None:
        self.menu_background = pygame.image.load(MENU_MAIN_BG)
        self.main_scene_background = pygame.image.load(MAIN_SCENE_BACKGROUND)

        self.sprite_man = pygame.image.load(SPRITE_MAN)
        self.sprite_man = pygame.transform.scale(self.sprite_man, SPRITE_SIZE)

        self.sprite_crow = pygame.image.load(SPRITE_CROW)
        self.sprite_crow = pygame.transform.scale(self.sprite_crow, SPRITE_SIZE)

        self.sprite_dog = pygame.image.load(SPRITE_DOG)
        self.sprite_dog = pygame.transform.scale(self.sprite_dog, SPRITE_SIZE)
        
        self.sprite_dragon = pygame.image.load(SPRITE_DRAGON)
        self.sprite_dragon = pygame.transform.scale(self.sprite_dragon, SPRITE_SIZE)


    ########################################################
    ######################## SCENES ########################
    ########################################################

    def __render_menu(self) -> None:
        """ main menu """
        self.screen.blit(self.menu_background, TOPLEFT)
        txt, txt_rect = text_center("PRESS SPACE TO START", BLACK)
        self.screen.blit(txt, txt_rect)


    def __render_play(self) -> None:
        """ initial dialog """
        self.screen.fill(BLACK)
        txt, txt_rect = text_center(DIALOG_INTRO[self.animation_index], WHITE)
        self.screen.blit(txt, txt_rect)


    def __render_level_one(self) -> None:
        """ talk to the man """
        self.screen.blit(self.main_scene_background, (0, -150))
        pygame.draw.rect(self.screen, BLACK, BOX_DIALOG)
        
        txt, txt_rect = text_bottom(DIALOG_LEVEL_ONE[self.animation_index], WHITE)
        self.screen.blit(txt, txt_rect)

        self.screen.blit(self.sprite_man, (0, 650))


    def __render_level_two(self) -> None:
        """ tal to the crow """
        self.screen.fill(BLACK)
        pygame.draw.rect(self.screen, LAVENDER, BOX_DIALOG)

        txt, txt_rect = text_bottom(DIALOG_LEVEL_TWO[self.animation_index], DARK_BLUE)
        self.screen.blit(txt, txt_rect)

        self.screen.blit(self.sprite_crow, (-10, 650))
        

    def __render_level_crow(self) -> None:
        """ first riddle """
        self.riddle.generate(riddle=DIALOG_LEVEL_CROW, npc=self.sprite_crow, answer_max="Word has 4 letters.")


    def __render_level_crow1(self) -> None:
        """ second riddle """
        self.riddle.generate(riddle=DIALOG_LEVEL_CROW1, npc=self.sprite_crow, answer_max="Word has 4 letters.")


    def __render_level_crow2(self) -> None:
        """ third riddle """
        self.riddle.generate(riddle=DIALOG_LEVEL_CROW2, npc=self.sprite_crow, answer_max="Word has 4 letters.")


    def __render_crow_end(self) -> None:
        """ tal to the crow """
        self.screen.fill(BLACK)
        pygame.draw.rect(self.screen, LAVENDER, BOX_DIALOG)

        txt, txt_rect = text_bottom(DIALOG_CROW_END[self.animation_index], DARK_BLUE)
        self.screen.blit(txt, txt_rect)

        self.screen.blit(self.sprite_crow, (-10, 650))


    def __render_level_dog(self) -> None:
        """ first riddle """
        self.riddle.generate(riddle=DIALOG_LEVEL_DOG, npc=self.sprite_dog, answer_max="Word has 3 letters.")


    def __render_level_dog1(self) -> None:
        """ second riddle """
        self.riddle.generate(riddle=DIALOG_LEVEL_DOG1, npc=self.sprite_dog, answer_max="Word has 6 letters.")


    def __render_level_dog2(self) -> None:
        """ third riddle """
        self.riddle.generate(riddle=DIALOG_LEVEL_DOG2, npc=self.sprite_dog, answer_max="Word has 7 letters.")


    def __render_dog_end(self) -> None:
        """ talk to the dog """
        self.screen.fill(BLACK)
        pygame.draw.rect(self.screen, LAVENDER, BOX_DIALOG)

        txt, txt_rect = text_bottom(DIALOG_DOG_END[self.animation_index], DARK_BLUE)
        self.screen.blit(txt, txt_rect)

        self.screen.blit(self.sprite_dog, (-10, 650))


    def __render_level_dragon(self) -> None:
        """ first riddle """
        self.riddle.generate(riddle=DIALOG_LEVEL_DRAGON, npc=self.sprite_dragon, answer_max="Word has 7 letters.")


    def __render_level_dragon1(self) -> None:
        """ second riddle """
        self.riddle.generate(riddle=DIALOG_LEVEL_DRAGON1, npc=self.sprite_dragon, answer_max="Word has 8 letters.")


    def __render_level_dragon2(self) -> None:
        """ third riddle """
        self.riddle.generate(riddle=DIALOG_LEVEL_DRAGON2, npc=self.sprite_dragon, answer_max="Word has 6 letters.")


    def __render_dragon_end(self) -> None:
        """ talk to the dragon """
        self.screen.fill(BLACK)
        pygame.draw.rect(self.screen, LAVENDER, BOX_DIALOG)

        txt, txt_rect = text_bottom(DIALOG_DRAGON_END[self.animation_index], DARK_BLUE)
        self.screen.blit(txt, txt_rect)

        self.screen.blit(self.sprite_dragon, (-10, 650))


    def __render_end_game(self) -> None:
        """ talk to the man """
        self.screen.blit(self.main_scene_background, (0, -150))
        pygame.draw.rect(self.screen, BLACK, BOX_DIALOG)
        
        txt, txt_rect = text_bottom(DIALOG_END_GAME[self.animation_index], WHITE)
        self.screen.blit(txt, txt_rect)

        self.screen.blit(self.sprite_man, (0, 650))







class Riddle:
    def __init__(self, screen, buffer) -> None:
        self.screen = screen
        self.answer_buffer = buffer

    def generate(self, riddle:list, answer_max:str, npc):

        self.screen.fill(BLACK)
        self.screen.blit(npc, (25, 695))

        display_position:tuple = [90, 0]
        for line in riddle:
            dialog = FONT_MAIN_NORMAL.render(line, True, WHITE)
            self.screen.blit(dialog, (display_position[0], display_position[1]))
            display_position[1] += 35

        txt, txt_rect = text_center(self.answer_buffer, WHITE)
        self.screen.blit(txt, txt_rect)

        hint = FONT_MAIN_NORMAL.render(answer_max, True, WHITE)
        self.screen.blit(hint, (SCREEN_WIDTH/2, SCREEN_HEIGHT-100))