import pygame
from components.constants import *
from components.game import Game
from tkinter import *
from tkinter import messagebox
Tk().wm_withdraw() #to hide the main window
from minimax.algorithm import minimax
from time import time

from config import *


WIN=pygame.display.set_mode((WIDTH,HEIGHT))
def get_click_pos(pos):
    '''
    returns row and column of board from x and y coordinates
    '''
    x,y=pos
    row=y//SQUARE_SIZE
    col=x//SQUARE_SIZE
    return row,col

def mainGame():
    game=Game(WIN)
    run=True
    clock=pygame.time.Clock()
    
    while run:
        clock.tick(FPS)
        if w:=game.winner():
            pygame.time.delay(1000)
            confirm=messagebox.askyesnocancel('Game OVER',w+" IS THE WINNER\nWant to restart??")
            if confirm:
                game.reset()
            else:
                run=False
        if game.turn==WHITE:
            game.thinking=True
            game.update()
            _, new_board=minimax(game.get_board(),AI_LEVEL,visualize=VISUALISE,game=game)
            game.thinking=False
            pygame.time.delay(200)
            game.ai_move(new_board)


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break
            if event.type==pygame.MOUSEBUTTONDOWN:
                row,col=get_click_pos(pygame.mouse.get_pos())
                game.select(row,col)
        game.update()
                
    pygame.quit()
    
if __name__=="__main__":
    mainGame()