import pygame
from pygame import mixer
from pygame.locals import *
import random

result = [] # A list to store the game result ('win' or 'lose').
win_count = [0] #A list to store the number of wins.
lose_count = [0] #A list to store the number of losses.

def game(goal_score):
    """The main game function that initializes the Pygame environment, sets up the game window, and manages the game loop."""
    pygame.init()

    # create the game window
    width = 800
    height = 720
    scoreboard_height = 80
    window_size = (width, height + scoreboard_height)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption('Match Three Game')

    # list of bat colors
    bat_colors = ['blue', 'green', 'orange', 'pink', 'purple', 'red', 'teal', 'yellow']

    # bat size
    bat_width = 80
    bat_height = 80
    bat_size = (bat_width, bat_height)

    class Bat:
        #represents a bat/game peice on the game board
        def __init__(self, row_num, col_num):
            # set the bats position on the board
            self.row_num = row_num
            self.col_num = col_num

            # assign a random image
            self.color = random.choice(bat_colors)
            image_name = f'Match_3_Peices/symbol_{self.color}.png'
            self.image = pygame.image.load(image_name)
            self.image = pygame.transform.smoothscale(self.image, bat_size)
            self.rect = self.image.get_rect()
            self.rect.left = col_num * bat_width
            self.rect.top = row_num * bat_height

        # draw the image on the screen
        def draw(self):
            screen.blit(self.image, self.rect)

        # snap the bat to its position on the board
        def snap(self):
            self.snap_row()
            self.snap_col()

        def snap_row(self):
            self.rect.top = self.row_num * bat_height

        def snap_col(self):
            self.rect.left = self.col_num * bat_width

    # create the board of bats
    board = []
    for row_num in range(height // bat_height):

        # add a new row to the board
        board.append([])

        for col_num in range(width // bat_width):
            # create the bat and add it to the board
            bat = Bat(row_num, col_num)
            board[row_num].append(bat)

    def draw():
        # draw the background
        pygame.draw.rect(screen, "black", (0, 0, width, height + scoreboard_height))

        # draw the candies
        for row in board:
            for bat in row:
                bat.draw()

        # display the score and moves
        font = pygame.font.SysFont('monoface', 40)
        goal_score_text = font.render(f'Goal Score:: {goal_score}', 1, "white")
        goal_score_text_rect = goal_score_text.get_rect(center=(width * 1 / 5, height + scoreboard_height / 2))
        screen.blit(goal_score_text, goal_score_text_rect)

        score_text = font.render(f'Score: {score}', 1, "white")
        score_text_rect = score_text.get_rect(center=(width * 1/2, height + scoreboard_height / 2))
        screen.blit(score_text, score_text_rect)

        moves_text = font.render(f'Moves: {moves}', 1, "white")
        moves_text_rect = moves_text.get_rect(center=(width * 4/5, height + scoreboard_height / 2))
        screen.blit(moves_text, moves_text_rect)


    # swap the positions of two bats
    def swap(bat1, bat2):
        temp_row = bat1.row_num
        temp_col = bat1.col_num

        bat1.row_num = bat2.row_num
        bat1.col_num = bat2.col_num

        bat2.row_num = temp_row
        bat2.col_num = temp_col

        # update the bats on the board list
        board[bat1.row_num][bat1.col_num] = bat1
        board[bat2.row_num][bat2.col_num] = bat2

        # snap them into their board positions
        bat1.snap()
        bat2.snap()

    # find neighboring bats that match the bats color
    def find_matches(bat, matches):
        # add the bat to the set
        matches.add(bat)

        # check the bat above if it's the same color
        if bat.row_num > 0:
            neighbor = board[bat.row_num - 1][bat.col_num]
            if bat.color == neighbor.color and neighbor not in matches:
                matches.update(find_matches(neighbor, matches))

        # check the bat below if it's the same color
        if bat.row_num < height / bat_height - 1:
            neighbor = board[bat.row_num + 1][bat.col_num]
            if bat.color == neighbor.color and neighbor not in matches:
                matches.update(find_matches(neighbor, matches))

        # check the bat to the left if it's the same color
        if bat.col_num > 0:
            neighbor = board[bat.row_num][bat.col_num - 1]
            if bat.color == neighbor.color and neighbor not in matches:
                matches.update(find_matches(neighbor, matches))

        # check the bat to the right if it's the same color
        if bat.col_num < width / bat_width - 1:
            neighbor = board[bat.row_num][bat.col_num + 1]
            if bat.color == neighbor.color and neighbor not in matches:
                matches.update(find_matches(neighbor, matches))

        return matches

    # return a set of at least 3 matching bats or an empty set
    def match_three(bat):
        matches = find_matches(bat, set())
        if len(matches) >= 3:
            return matches
        else:
            return set()

    # bat that the user clicked on
    clicked_bat = None

    # the adjacent bat that will be swapped with the clicked bat
    swapped_bat = None

    # coordinates of the point where the user clicked on
    click_x = None
    click_y = None

    # game variables
    score = 0
    moves = 0

    # game loop
    clock = pygame.time.Clock()
    running = True
    while running:

        # set of matching bats
        matches = set()

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            # detect mouse click
            if clicked_bat is None and event.type == MOUSEBUTTONDOWN:

                # get the bat that was clicked on
                for row in board:
                    for bat in row:
                        if bat.rect.collidepoint(event.pos):
                            clicked_bat = bat

                            # save the coordinates of the point where the user clicked
                            click_x = event.pos[0]
                            click_y = event.pos[1]

            # detect mouse motion
            if clicked_bat is not None and event.type == MOUSEMOTION:

                # calculate the distance between the point the user clicked on
                # and the current location of the mouse cursor
                distance_x = abs(click_x - event.pos[0])
                distance_y = abs(click_y - event.pos[1])

                # reset the position of the swapped bat if direction of mouse motion changed
                if swapped_bat is not None:
                    swapped_bat.snap()

                # determine the direction of the neighboring bat to swap with
                if distance_x > distance_y and click_x > event.pos[0]:
                    direction = 'left'
                elif distance_x > distance_y and click_x < event.pos[0]:
                    direction = 'right'
                elif distance_y > distance_x and click_y > event.pos[1]:
                    direction = 'up'
                else:
                    direction = 'down'

                # if moving left/right, snap the clicked bat to its row position
                # otherwise, snap it to its col position
                if direction in ['left', 'right']:
                    clicked_bat.snap_row()
                else:
                    clicked_bat.snap_col()

                # if moving the clicked bat to the left,
                # make sure it's not on the first col
                if direction == 'left' and clicked_bat.col_num > 0:

                    # get the bat to the left
                    swapped_bat = board[clicked_bat.row_num][clicked_bat.col_num - 1]

                    # move the two bats
                    clicked_bat.rect.left = clicked_bat.col_num * bat_width - distance_x
                    swapped_bat.rect.left = swapped_bat.col_num * bat_width + distance_x

                    # snap them into their new positions on the board
                    if clicked_bat.rect.left <= swapped_bat.col_num * bat_width + bat_width / 4:
                        swap(clicked_bat, swapped_bat)
                        matches.update(match_three(clicked_bat))
                        matches.update(match_three(swapped_bat))
                        moves += 1
                        clicked_bat = None
                        swapped_bat = None

                # if moving the clicked bat to the right,
                # make sure it's not on the last col
                if direction == 'right' and clicked_bat.col_num < width / bat_width - 1:

                    # get the bat to the right
                    swapped_bat = board[clicked_bat.row_num][clicked_bat.col_num + 1]

                    # move the two bats
                    clicked_bat.rect.left = clicked_bat.col_num * bat_width + distance_x
                    swapped_bat.rect.left = swapped_bat.col_num * bat_width - distance_x

                    # snap them into their new positions on the board
                    if clicked_bat.rect.left >= swapped_bat.col_num * bat_width - bat_width / 4:
                        swap(clicked_bat, swapped_bat)
                        matches.update(match_three(clicked_bat))
                        matches.update(match_three(swapped_bat))
                        moves += 1
                        clicked_bat = None
                        swapped_bat = None

                # if moving the clicked bat up,
                # make sure it's not on the first row
                if direction == 'up' and clicked_bat.row_num > 0:

                    # get the bat above
                    swapped_bat = board[clicked_bat.row_num - 1][clicked_bat.col_num]

                    # move the two bats
                    clicked_bat.rect.top = clicked_bat.row_num * bat_height - distance_y
                    swapped_bat.rect.top = swapped_bat.row_num * bat_height + distance_y

                    # snap them into their new positions on the board
                    if clicked_bat.rect.top <= swapped_bat.row_num * bat_height + bat_height / 4:
                        swap(clicked_bat, swapped_bat)
                        matches.update(match_three(clicked_bat))
                        matches.update(match_three(swapped_bat))
                        moves += 1
                        clicked_bat = None
                        swapped_bat = None

                # if moving the clicked bat down,
                # make sure it's not on the last row
                if direction == 'down' and clicked_bat.row_num < height / bat_height - 1:

                    # get the bat below
                    swapped_bat = board[clicked_bat.row_num + 1][clicked_bat.col_num]

                    # move the two bats
                    clicked_bat.rect.top = clicked_bat.row_num * bat_height + distance_y
                    swapped_bat.rect.top = swapped_bat.row_num * bat_height - distance_y

                    # snap them into their new positions on the board
                    if clicked_bat.rect.top >= swapped_bat.row_num * bat_height - bat_height / 4:
                        swap(clicked_bat, swapped_bat)
                        matches.update(match_three(clicked_bat))
                        matches.update(match_three(swapped_bat))
                        moves += 1
                        clicked_bat = None
                        swapped_bat = None

            if moves <= 10 and score >= goal_score:  # end game after 10 moves and update win/lose counts
                result.append("win")
                win_count[0] += 1
                return
            elif moves == 11 and score < goal_score:
                result.append("lose")
                lose_count[0] += 1
                return

            # detect mouse release
            if clicked_bat is not None and event.type == MOUSEBUTTONUP:

                # snap the bats back to their original positions on the grid
                clicked_bat.snap()
                clicked_bat = None
                if swapped_bat is not None:
                    swapped_bat.snap()
                    swapped_bat = None

        draw()
        pygame.display.update()

        # check if there's at least 3 matching bats
        if len(matches) >= 3:
            sound_effects = ["dsskepch", "boxing_hitwall1", "dspunch", "hit", "tm2_hit004"]
            hit_sound = random.choice(sound_effects)
            sound = mixer.Sound(f"Music/{hit_sound}.wav")  # music for matches
            sound.play()

            # add to score
            score += len(matches)

            # animate the matching bats shrinking
            while len(matches) > 0:
                clock.tick(100)

                # decrease width and height by 1
                for bat in matches:
                    new_width = bat.image.get_width() - 1
                    new_height = bat.image.get_height() - 1
                    new_size = (new_width, new_height)
                    bat.image = pygame.transform.smoothscale(bat.image, new_size)
                    bat.rect.left = bat.col_num * bat_width + (bat_width - new_width) / 2
                    bat.rect.top = bat.row_num * bat_height + (bat_height - new_height) / 2

                # check if the bats have shrunk to zero size
                for row_num in range(len(board)):
                    for col_num in range(len(board[row_num])):
                        bat = board[row_num][col_num]
                        if bat.image.get_width() <= 0 or bat.image.get_height() <= 0:
                            matches.remove(bat)


                            # generate a new bat
                            board[row_num][col_num] = Bat(row_num, col_num)

                draw()
                pygame.display.update()

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.quit()