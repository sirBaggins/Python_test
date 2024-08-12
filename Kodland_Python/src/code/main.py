# external imports
import pygame

# internal imports
from settings import *
from helpers import *
from dialogs import *

# class imports
from scenes import Scenes


def main():
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_WIDTH_HEIGHT)
    pygame.display.set_caption(GAME_NAME)
    
    game_running:bool = True
    timer = pygame.time.Clock()

    scene:Scenes = Scenes(screen=screen)
    keyboard_free:bool = True # prevents double input

    play_song(SONG_AURA_PATH)

    #### GAME LOOP ####
    while (game_running):

        scene.render(current_scene(scene.scene_counter))

        ## EVENT HANDLER ##
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

            """ requires a refactor, looks terrible """

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
                        keyboard_free = False
                        scene.scene_counter = set_scene("level_one")

            if (current_scene(scene.scene_counter) == "level_one"):
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE) and (keyboard_free):
                    if scene.animation_index < (len(DIALOG_LEVEL_ONE) - 1):
                        scene.animation_index += 1
                    else:
                        scene.animation_index = 0
                        keyboard_free = False
                        scene.scene_counter = set_scene("level_two")

            if (current_scene(scene.scene_counter) == "level_two"):
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE) and (keyboard_free):
                    if scene.animation_index < (len(DIALOG_LEVEL_TWO) - 1):
                        scene.animation_index += 1
                    else:
                        scene.animation_index = 0
                        keyboard_free = False
                        scene.scene_counter = set_scene("level_crow")


            if (current_scene(scene.scene_counter) == "level_crow"):
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_BACKSPACE):
                        scene.riddle.answer_buffer = scene.riddle.answer_buffer[:-1]

                    elif (event.key == pygame.K_RETURN) and (len(scene.riddle.answer_buffer) == 4):
                        if scene.riddle.answer_buffer.lower() == "book":
                            scene.scene_counter = set_scene("level_crow1")

                    else:
                        if (len(scene.riddle.answer_buffer) < 4):
                            scene.riddle.answer_buffer += event.unicode

            if (current_scene(scene.scene_counter) == "level_crow1"):
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_BACKSPACE):
                        scene.riddle.answer_buffer = scene.riddle.answer_buffer[:-1]

                    elif (event.key == pygame.K_RETURN) and (len(scene.riddle.answer_buffer) == 4):
                        if scene.riddle.answer_buffer.lower() == "time":
                            scene.scene_counter = set_scene("level_crow2")

                    else:
                        if (len(scene.riddle.answer_buffer) < 4):
                            scene.riddle.answer_buffer += event.unicode

            if (current_scene(scene.scene_counter) == "level_crow2"):
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_BACKSPACE):
                        scene.riddle.answer_buffer = scene.riddle.answer_buffer[:-1]

                    elif (event.key == pygame.K_RETURN) and (len(scene.riddle.answer_buffer) == 4):
                        if scene.riddle.answer_buffer.lower() == "past":
                            scene.riddle.answer_buffer = "type"
                            scene.scene_counter = set_scene("crow_end")

                    else:
                        if (len(scene.riddle.answer_buffer) < 4):
                            scene.riddle.answer_buffer += event.unicode

            if (current_scene(scene.scene_counter) == "crow_end"):
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE) and (keyboard_free):
                    if scene.animation_index < (len(DIALOG_CROW_END) - 1):
                        scene.animation_index += 1
                    else:
                        scene.animation_index = 0
                        keyboard_free = False
                        scene.riddle.answer_buffer = "type"
                        scene.scene_counter = set_scene("level_dog")

            if (current_scene(scene.scene_counter) == "level_dog"):
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_BACKSPACE):
                        scene.riddle.answer_buffer = scene.riddle.answer_buffer[:-1]

                    elif (event.key == pygame.K_RETURN) and (len(scene.riddle.answer_buffer) == 3):
                        if scene.riddle.answer_buffer.lower() == "now":
                            scene.riddle.answer_buffer = "type"
                            scene.scene_counter = set_scene("level_dog1")

                    else:
                        if (len(scene.riddle.answer_buffer) < 3):
                            scene.riddle.answer_buffer += event.unicode

            if (current_scene(scene.scene_counter) == "level_dog1"):
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_BACKSPACE):
                        scene.riddle.answer_buffer = scene.riddle.answer_buffer[:-1]

                    elif (event.key == pygame.K_RETURN) and (len(scene.riddle.answer_buffer) == 6):
                        if scene.riddle.answer_buffer.lower() == "record":
                            scene.riddle.answer_buffer = "type"
                            scene.scene_counter = set_scene("level_dog2")

                    else:
                        if (len(scene.riddle.answer_buffer) < 6):
                            scene.riddle.answer_buffer += event.unicode
        
            if (current_scene(scene.scene_counter) == "level_dog2"):
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_BACKSPACE):
                        scene.riddle.answer_buffer = scene.riddle.answer_buffer[:-1]

                    elif (event.key == pygame.K_RETURN) and (len(scene.riddle.answer_buffer) == 7):
                        if scene.riddle.answer_buffer.lower() == "present":
                            scene.riddle.answer_buffer = "type"
                            scene.scene_counter = set_scene("dog_end")

                    else:
                        if (len(scene.riddle.answer_buffer) < 7):
                            scene.riddle.answer_buffer += event.unicode

            if (current_scene(scene.scene_counter) == "dog_end"):
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE) and (keyboard_free):
                    if scene.animation_index < (len(DIALOG_DOG_END) - 1):
                        scene.animation_index += 1
                    else:
                        scene.animation_index = 0
                        keyboard_free = False
                        scene.riddle.answer_buffer = "type"
                        scene.scene_counter = set_scene("level_dragon")

            if (current_scene(scene.scene_counter) == "level_dragon"):
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_BACKSPACE):
                        scene.riddle.answer_buffer = scene.riddle.answer_buffer[:-1]

                    elif (event.key == pygame.K_RETURN) and (len(scene.riddle.answer_buffer) == 7):
                        if scene.riddle.answer_buffer.lower() == "horizon":
                            scene.riddle.answer_buffer = "type"
                            scene.scene_counter = set_scene("level_dragon1")

                    else:
                        if (len(scene.riddle.answer_buffer) < 7):
                            scene.riddle.answer_buffer += event.unicode

            if (current_scene(scene.scene_counter) == "level_dragon1"):
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_BACKSPACE):
                        scene.riddle.answer_buffer = scene.riddle.answer_buffer[:-1]

                    elif (event.key == pygame.K_RETURN) and (len(scene.riddle.answer_buffer) == 8):
                        if scene.riddle.answer_buffer.lower() == "calendar":
                            scene.riddle.answer_buffer = "type"
                            scene.scene_counter = set_scene("level_dragon2")

                    else:
                        if (len(scene.riddle.answer_buffer) < 8):
                            scene.riddle.answer_buffer += event.unicode

            if (current_scene(scene.scene_counter) == "level_dragon2"):
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_BACKSPACE):
                        scene.riddle.answer_buffer = scene.riddle.answer_buffer[:-1]

                    elif (event.key == pygame.K_RETURN) and (len(scene.riddle.answer_buffer) == 6):
                        if scene.riddle.answer_buffer.lower() == "future":
                            scene.riddle.answer_buffer = "type"
                            scene.scene_counter = set_scene("dragon_end")

                    else:
                        if (len(scene.riddle.answer_buffer) < 6):
                            scene.riddle.answer_buffer += event.unicode


            if (current_scene(scene.scene_counter) == "dragon_end"):
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE) and (keyboard_free):
                    if scene.animation_index < (len(DIALOG_DRAGON_END) - 1):
                        scene.animation_index += 1
                    else:
                        scene.animation_index = 0
                        keyboard_free = False
                        scene.scene_counter = set_scene("end_game")

                
            if (current_scene(scene.scene_counter) == "end_game"):
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE) and (keyboard_free):
                    if scene.animation_index < (len(DIALOG_END_GAME) - 1):
                        scene.animation_index += 1
                    else:
                        pygame.quit()

        ###################


        pygame.display.flip()
        timer.tick(FPS)
    #### END LOOP ####

    pygame.quit()
    return



if __name__ == "__main__":
    main()