import pygame
import Fade

"""The Game_Results module provides functions to handle the display and transitions for various game results, contributing to the overall gaming experience. """

def Win_Round():
    """Handles the display of winning round messages by setting the game window caption, loading an image, and utilizing
     'Fade' module for smooth transitions."""
    pygame.display.set_caption("You've won the round!!!")
    win_round = pygame.image.load("Images/Win_Round.png")
    Fade.fadein(win_round, 800)
    Fade.fadeout(win_round, 800)
    return

def Lose_Round():
    """Handle the display of losing rounds messages by setting the game window caption, loading an image, and utilizing
    'Fade' module for smooth transitions."""
    pygame.display.set_caption("You've lost the round...")
    lose_round = pygame.image.load("Images/Lose_Round.png")
    Fade.fadein(lose_round, 800)
    Fade.fadeout(lose_round, 800)
    return

def Win_Game_Setup():
    pygame.display.set_caption("You won the Final Bat-le!!!")
    win_game = pygame.image.load("Images/Win_Game.png")
    Fade.fadein(win_game, 800)
    return

def Win_Game():
    """This function manages the display of winning the entire game. Win_Game_Setup initializes the window caption and
     fades in the winning game image. Win_Game continues to display the winning message until the user closes the window."""
    #screen setup
    pygame.init()
    screen_width = 800
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    running = True


    while running:
        #Displays winning game message
        screen.fill("grey")
        pygame.display.set_caption("You won the Final Bat-le!!!")
        win_game = pygame.image.load("Images/Win_Game.png")
        screen.blit(win_game, (screen_width / 2 - 400, screen_height / 2 - 400))
        pygame.display.update()

        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


    pygame.quit()

def Lose_Game_Setup():
    pygame.display.set_caption("You lost the Final Bat-le...")
    lose_game = pygame.image.load("Images/Lose_Game.png")
    Fade.fadein(lose_game, 800)
    return

def Lose_Game():
    """This function manages the display of winning the entire game. Win_Game_Setup initializes the window caption and
    fades in the winning game image. Win_Game continues to display the winning message until the user closes the window."""
    #screen setup
    pygame.init()
    screen_width = 800  # so we dont hardcode screen size
    screen_height = 800  # so we dont hardcode screen size
    screen = pygame.display.set_mode((screen_width, screen_height))
    running = True

    while running:
        #display losing game message
        screen.fill("grey")
        pygame.display.set_caption("You lost the Final Bat-le...")
        lose_game = pygame.image.load("Images/Lose_Game.png")
        screen.blit(lose_game, (screen_width / 2 - 400, screen_height / 2 - 400))
        pygame.display.update()  # updates screen image/displays it

        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


    pygame.quit()