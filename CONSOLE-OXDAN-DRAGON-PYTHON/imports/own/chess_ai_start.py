import random

import chess
from pygame.locals import (
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from imports.chess.modules.board_tools import *
from imports.chess.modules.drawing_tools import *
from imports.chess.modules.piece import *
from imports.chess.engine import is_stable
from imports.chess.engine import find_depth_move
import imports.own.will_go_to_start
import os
from colorama import Fore

def chess_ai_start():

    os.system("cls")
    # Initializes the pygame library
    pygame.init()

    # Returns a surface to work on
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initialize board squares and board
    chess_board = make_board_squares(SCREEN_WIDTH, SCREEN_HEIGHT)
    board = chess.Board()

    # Draws squares, then pieces on top of squares
    draw_squares(screen, chess_board)
    draw_position_by_fen(screen, chess_board, board.fen())

    # Game loop
    running = True
    while running:

        pygame.display.set_caption('Chess ai')
        ico = pygame.image.load(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],'my_dragon_ico.jpg')).convert()
        pygame.display.set_icon (ico)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    pygame.quit()
                    imports.own.will_go_to_start.main()

            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                square1 = get_square_for_position(chess_board, pos).position
            if event.type == MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                square2 = get_square_for_position(chess_board, pos).position

                # Chess.Move throws an error that crashes the program is the move is the same square twice
                if square1 == square2:
                    continue
                move_string = square1.lower() + square2.lower()
                move = chess.Move.from_uci(move_string)  # creates player move
                # move.promotion = 5

                moves = list(board.legal_moves)
                if move in moves:
                    board.push(move)
                elif chess.Move.from_uci(move_string + 'q') in moves:
                    move = chess.Move.from_uci(move_string + 'q')
                    board.push(move)
                else:
                    # If this line weren't here the engine would just make a move for white when you make an illegal move
                    continue

                # Just draw the board again lmao part 1
                draw_squares(screen, chess_board)
                draw_position_by_fen(screen, chess_board, board.fen())

                if board.is_checkmate():
                    print(Fore.YELLOW + "Good game! You Win!" + Fore.WHITE)
                    imports.own.will_go_to_start.main()
                elif board.is_stalemate():
                    print(Fore.YELLOW + "Good game! Draw!" + Fore.WHITE)
                    imports.own.will_go_to_start.main()
                else:
                    # Calculate engine move and make it if not checkmate
                    engine_move = find_depth_move(board, 3)
                    board.push(engine_move)

                # Just draw the board again lmao part 2
                draw_squares(screen, chess_board)
                draw_position_by_fen(screen, chess_board, board.fen())

                if board.is_checkmate():
                    print(Fore.YELLOW + "Good game!" + Fore.RED + " You Lose!" + Fore.WHITE)
                    imports.own.will_go_to_start.main()

            elif event.type == QUIT:

                running = False
                pygame.quit()
                imports.own.will_go_to_start.main()

