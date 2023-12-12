import Fade
import random
import pygame

"""The Villain module is responsible for randomly selecting and displaying villains during the game."""

Villians = ["The Joker", "Poison Ivy", "The Riddler", "Catwoman", "Two-Face"]
villian_list = []
for item in range(5):
    villian_list.append(random.choice(Villians)) #Picks random villian
    Villians.remove(villian_list[-1])
    """This section initializes a list of villains (Villains) and randomly selects five villains without repetition, 
    storing them in villain_list. This ensures that each villain appears exactly once during the game."""

def rand_villian(list_num): #displays the villian being fought
    """This function, rand_villain(list_num), displays the villain corresponding to the index list_num from the
    villain_list. It sets the game window caption to "New Challenger" and uses the Fade module to smoothly fade in and out the villain image."""
    pygame.display.set_caption('New Challenger')
    if villian_list[list_num] == "The Joker":
        joker = pygame.image.load("Characters/Joker.png")
        Fade.fadein(joker, 800)
        Fade.fadeout(joker, 800)
        return

    elif villian_list[list_num] == "Poison Ivy":
        poison_ivy = pygame.image.load("Characters/Poison_ivy.png")
        Fade.fadein(poison_ivy, 800)
        Fade.fadeout(poison_ivy, 800)
        return

    elif villian_list[list_num] == "The Riddler":
        riddler = pygame.image.load("Characters/Riddler.png")
        Fade.fadein(riddler, 800)
        Fade.fadeout(riddler, 800)
        return

    elif villian_list[list_num] == "Catwoman":
        catwoman = pygame.image.load("Characters/Catwoman.png")
        Fade.fadein(catwoman, 800)
        Fade.fadeout(catwoman, 800)
        return

    elif villian_list[list_num] == "Two-Face":
        two_face = pygame.image.load("Characters/Two_Face.png")
        Fade.fadein(two_face, 800)
        Fade.fadeout(two_face, 800)
        return
