import pygame
from components.constants import *
from components.game import Game
from tkinter import *
from tkinter import messagebox
Tk().wm_withdraw() #to hide the main window
from minimax.algorithm import minimax


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
        if game.turn==WHITE:
            value, new_board=minimax(game.get_board(),6,visualize=False,game=game)
            game.ai_move(new_board)
        if w:=game.winner():
            confirm=messagebox.askyesnocancel('Game OVER',w+" IS THE WINNER\nWant to restart??")
            if confirm:
                game.reset()
            else:
                run=False
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