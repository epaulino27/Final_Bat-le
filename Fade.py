import pygame

"""The Fade module provides functions for smoothly fading in and out of images on the screen. """

#screen setip
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
win = pygame.display.set_mode([screen_width,screen_height])

def fadeout(image, imagesize, time = 5, width = screen_width, height = screen_height):
    """This function, fadeout, takes an image, its size, and optional parameters for time, width, and height. It
    gradually fades out the image while updating the screen."""
    fade = pygame.Surface((width, height)) #decides how much of screen fades
    fade.fill("black") #fades to black
    for alpha in range(0, 300): #iterates making it fade slowly
        fade.set_alpha(alpha)

        screen.fill("grey")
        screen.blit(image, (screen_width/2 - imagesize/2, screen_height/2 - imagesize/2))

        win.blit(fade, (0,0)) #draws fade
        pygame.display.update() #updates screen image
        pygame.time.delay(time) #

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

def fadein(image, imagesize, time = 5, width = screen_width, height = screen_height):
    """This function, fadein, takes an image, its size, and optional parameters for time, width, and height. It
    gradually fades in the image while updating the screen."""
    fade = pygame.Surface((width, height)) #decides how much of screen fades
    fade.fill("grey")  # fades to black
    fade.blit(image, (screen_width / 2 - imagesize / 2, screen_height / 2 - imagesize / 2))
    for alpha in range(0, 300): #iterates making it fade slowly
        fade.set_alpha(alpha)

        screen.fill("black")

        win.blit(fade, (0,0)) #draws fade
        pygame.display.update() #updates screen image
        pygame.time.delay(time) #

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False