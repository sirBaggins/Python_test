# external imports
import pygame

# internal imports
from settings import *
from helpers import *
from dialogs import *

# class imports
from scenes import Scenes

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_WIDTH_HEIGHT)
    pygame.display.set_caption(GAME_NAME)
    
    game_running:bool = True
    timer = pygame.time.Clock()

    scene:Scenes = Scenes(screen=screen)
    keyboard_free:bool = True # prevents double input

    #### GAME LOOP ####
    while (game_running):

        scene.render(current_scene(scene.scene_counter))

        ## EVENT HANDLER ##
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

            if (event.type == pygame.KEYUP) and (event.key == pygame.K_SPACE):
                keyboard_free = True

            if (current_scene(scene.scene_counter) == "menu"):
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
                    keyboard_free = False
                    scene.scene_counter = set_scene("play")

            if (current_scene(scene.scene_counter) == "play"):
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE) and (keyboard_free):
                    if scene.animation_index < (len(DIALOG_INTRO) - 1):
                        scene.animation_index += 1
                    else:
                        scene.animation_index = 0
                        scene.scene_counter = set_scene("level_one")

        ####################


        pygame.display.flip()
        timer.tick(FPS)
    #### END LOOP ####

    pygame.quit()
    return



if __name__ == "__main__":
    main()