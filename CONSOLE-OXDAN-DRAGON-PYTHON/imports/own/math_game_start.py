#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from imports.own.imports.math_game.game import Game
import imports.own.will_go_to_start
import os

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

def main_rt():
    # Initialize all imported pygame modules
    pygame.init()
    # Set the width and height of the screen [width, height]
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    # Set the current window caption
    pygame.display.set_caption("Math Game")
    # Load the icon image
    icon_image = pygame.image.load(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],"imports/own/my_dragon_ico_transformed.png"))

    # Set the icon
    pygame.display.set_icon(icon_image)
    #Loop until the user clicks the close button.
    done = False
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # Create game object
    game = Game()
    # -------- Main Program Loop -----------
    while not done:
        # --- Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()
        # --- Game logic should go here
        game.run_logic()
        # --- Draw the current frame
        game.display_frame(screen)
        # --- Limit to 30 frames per second
        clock.tick(30)

    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()
    imports.own.will_go_to_start.main()

def math_game_start():

    main_rt()
