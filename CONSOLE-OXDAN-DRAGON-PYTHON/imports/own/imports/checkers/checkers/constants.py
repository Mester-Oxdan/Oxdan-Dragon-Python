# All constant values are stored in this folder.
import pygame
import os

files_dir = os.path.dirname(__file__)
os.environ["OXDAN-DRAGON-PYTHON"] = files_dir 

#path_to_png = os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],"..","IMAGES","ALL","icon.png")

WIDTH, HEIGHT = 800, 800 # 800 pixels high by 800 pixels wide
ROWS, COLS = 8, 8 # 8 rows by 8 columns = std checkers board
SQUARE_SIZE = WIDTH//COLS # defines the area of one square

# RGB Color Scheme for Pygame
RED = (255, 0, 0) # define red color for pygame
WHITE = (255, 255, 255) # define white
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"], 'assets/crown.png')), (44, 25))
