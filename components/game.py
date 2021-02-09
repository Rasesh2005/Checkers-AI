import pygame

from .constants import *
from .board import Board
from .piece import Piece

class Game:
    def __init__(self,win) -> None:
        self.selected=None
        self.board=Board()
        self.turn=RED
        self.valid_moves={}
        self.WIN=win

    def update(self):
        self.board.draw(self.WIN)
        if self.selected:
            self.board.draw_selected_square(self.WIN,self.selected)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()
    def reset(self):
        self.selected=None
        self.board=Board()
        self.turn=RED
        self.valid_moves={}
    def select(self,row,col):
        if self.selected:
            temp=self.selected
            result=self.__move(row,col)
            if result:
                self.selected=None
            else:
                self.selected=temp
        piece=self.board.get_board_piece(row,col)
        if piece!=0 and piece.color==self.turn:
            self.selected=piece
            self.valid_moves=self.board.get_valid_moves(piece)
            return True

    def draw_valid_moves(self,moves:dict):
        for move in moves:
            row,col=move
            pygame.draw.circle(self.WIN,BLUE,(col*SQUARE_SIZE+SQUARE_SIZE//2,row*SQUARE_SIZE+SQUARE_SIZE//2),10)

    def winner(self):
        return self.board.winner()
    
    def get_board(self):
        return self.board
    def ai_move(self,board):
        self.board=board
        self.change_turn()
    def __move(self,row,col):
        piece=self.board.get_board_piece(row,col)
        if piece==0 and self.selected and (row,col) in self.valid_moves:
            self.board.move_piece(self.selected,row,col)
            self.change_turn()
            skipped=self.valid_moves.get((row,col))
            self.valid_moves={}
            if skipped:
                self.board.remove(skipped)
        else:
            return False
        return True
    
    def change_turn(self):
        if self.turn==RED:
            self.turn=WHITE
        else:
            self.turn=RED

