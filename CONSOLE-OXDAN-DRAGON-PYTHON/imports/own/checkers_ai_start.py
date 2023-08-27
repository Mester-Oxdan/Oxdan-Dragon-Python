import os
import pygame
import imports.own.will_go_to_start
import pygame
from colorama import Fore
from imports.own.imports.checkers.checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from imports.own.imports.checkers.checkers.game import Game
from imports.own.imports.checkers.minimax.algorithm import minimax

def checkers_ai_start():

    # Create a main loop that checks for user input (mouse, keyboard, etc) 
    # Draw all the pieces, the board, etc.

    FPS = 60 # do we need this in the constants file? No, only references drawing the game

    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

    # set caption for display here: shows up in top title bar
    pygame.display.set_caption('Checkers with ai')

    ico = pygame.image.load(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],'imports/own/my_dragon_ico.jpg')).convert()
    pygame.display.set_icon (ico)

    def get_row_col_from_mouse(pos):
        x, y = pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col

    def main_checkers_ai (): ## define main event loop
        run = True
        clock = pygame.time.Clock()
        game = Game(WINDOW)

        while run:
            clock.tick(FPS)

            if game.turn == WHITE: # Start AI HERE:
                value, new_board = minimax(game.get_board(), 3, WHITE, game)
                game.ai_move(new_board)
    
            if game.winner() != None:
                print(game.winner()) # prints red (255, 0, 0) or white (255, 255, 255) to the terminal
                run = False # Terminates the game

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False # Teminate Game
                    pygame.quit()
                    imports.own.will_go_to_start.main()

                if event.type == pygame.MOUSEBUTTONDOWN: # Select game piece with mouse
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)

            game.update()

        pygame.quit()
        imports.own.will_go_to_start.main()

    main_checkers_ai()

    