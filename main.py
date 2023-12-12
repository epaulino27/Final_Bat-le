import random
import pygame
import Fade
import Game_Results
import Villian
import Match_3
from pygame import mixer
"""This section imports necessary modules for the game, including Pygame for graphical elements, a custom Fade module 
for screen transitions, and other modules responsible for game results, villains, and the match-3 gameplay."""

# pygame setup
pygame.init()
#screen sizing
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
running = True

while running:
    # Title screen setup
    screen.fill("grey")
    pygame.display.set_caption("Game Title")
    gametitle = pygame.image.load("Images/Game_Title.png")
    screen.blit(gametitle, (screen_width/2 - 200,screen_height/2 - 200))
    pygame.display.update()

    if pygame.mouse.get_pressed()[0]:
        #Introductory sequence
        #background music for intro
        mixer.music.load("Music/The_Batman_Theme.ogg")
        mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.75)

        #display quest
        pygame.display.set_caption("Quest")
        Fade.fadeout(gametitle, 400)
        quest = pygame.image.load("Images/Quest.png")
        Fade.fadein(quest, 800, 3)
        Fade.fadeout(quest, 800, 30)
        pygame.display.flip()

        #display instructions
        pygame.display.set_caption("Game Instructions")
        instructions = pygame.image.load("Images/instructions.png")
        Fade.fadein(instructions, 800, 3)
        Fade.fadeout(instructions, 800, 30)
        pygame.display.flip()

        # set game difficulties and initialize variables
        difficulty = [50, 45, 40, 35, 30]  # list of difficulties for the goal score
        villian_num = 0
        songs = ["03 - First Confrontation", "10 - Descent into Mystery", "06 - Clown Attack", "02 - Roof Fight", "19 - The Final Confrontation"]
        song_num = 0

        for i in range(2): #Rounds 1-2
            # background music
            pygame.mixer.music.fadeout(5000)
            pygame.mixer.music.unload()
            mixer.music.load(f"Music/{songs[song_num]}.ogg")
            mixer.music.play(-1)
            song_num += 1
            # display villian
            Villian.rand_villian(villian_num)
            villian_num += 1  # increase villian number so different villian next time
            pygame.display.flip()
            # Round 1 and 2 gameplay
            Match_3.game(random.choice(difficulty))
            # Win/Lose round 1 and 2
            if Match_3.result[-1] == "win":
                Game_Results.Win_Round()
            else:
                Game_Results.Lose_Round()

        for i in range(3): #Rounds 3-5
            # background music
            pygame.mixer.music.fadeout(5000)
            pygame.mixer.music.unload()  # stop previous music
            mixer.music.load(f"Music/{songs[song_num]}.ogg")
            mixer.music.play(-1)
            song_num += 1
            # display villian
            Villian.rand_villian(villian_num)
            pygame.display.flip()
            # Round 3, 4, and 5 gameplay
            Match_3.game(random.choice(difficulty))
            villian_num += 1
            # Win/Lose round 3, 4, and 5
            if Match_3.win_count == [3]:
                pygame.mixer.music.fadeout(3000)
                pygame.mixer.music.unload() #stop previous music
                mixer.music.load("Music/app-34.wav")
                mixer.music.play() #clapping for win before silence
                Game_Results.Win_Game_Setup()
                Game_Results.Win_Game()
            elif Match_3.lose_count == [3]:
                pygame.mixer.music.fadeout(3000)
                pygame.mixer.music.unload()  # stop previous music
                mixer.music.load("Music/boo3.wav")
                mixer.music.play()  # sad for lose before silence
                Game_Results.Lose_Game_Setup()
                Game_Results.Lose_Game()
            elif Match_3.result[-1] == "win":
                Game_Results.Win_Round()
            else:
                Game_Results.Lose_Round()

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
