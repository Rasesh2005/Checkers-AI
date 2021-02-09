from config import WINDOW_SIZE
import pygame

WIDTH = HEIGHT = WINDOW_SIZE
ROWS=COLS=8
SQUARE_SIZE = WIDTH//ROWS


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128)

# King piece Crown Image
CROWN=pygame.transform.scale(pygame.image.load('assets/crown.png'),(40,40))
