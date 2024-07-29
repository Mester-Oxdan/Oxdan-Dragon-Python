
import pygame as pg
from . import setup, tools
from . import constants as c
from .states import main_menu, load_screen, level
import sys

def main():
    while True:
        pg.init()
        screen = pg.display.set_mode((800, 600))  # Set the screen size as needed
        pg.display.set_caption("Mario")

        game = tools.Control()
        state_dict = {c.MAIN_MENU: main_menu.Menu(),
                      c.LOAD_SCREEN: load_screen.LoadScreen(),
                      c.LEVEL: level.Level(),
                      c.GAME_OVER: load_screen.GameOver(),
                      c.TIME_OUT: load_screen.TimeOut()}
        game.setup_states(state_dict, c.MAIN_MENU)
        
        game.main()
        
        if game.done:
            pg.quit()  # Properly quit Pygame to clean up
            break  # Exit the loop if the game is done