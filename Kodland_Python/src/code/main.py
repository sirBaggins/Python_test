# external imports
import pygame

# internal imports
from settings import *
from helpers import *

# class imports
from scenes import Scenes

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_WIDTH_HEIGHT)
    pygame.display.set_caption(GAME_NAME)
    
    game_running:bool = True
    timer = pygame.time.Clock()

    scene:Scenes = Scenes(screen=screen)

    scene_counter:int = 0
    #### GAME LOOP ####
    while (game_running):
        timer.tick(FPS)
        
        scene.render(current_scene(scene_counter))

        ## EVENT HANDLER ##
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

            if (current_scene(scene_counter) == "menu"):
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
                    scene_counter = set_scene("play")

        ####################


        pygame.display.flip()
    #### END LOOP ####

    pygame.quit()
    return



if __name__ == "__main__":
    main()