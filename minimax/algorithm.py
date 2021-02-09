from config import VIS_DELAY
from components.constants import GREEN,RED, SQUARE_SIZE,WHITE
from copy import deepcopy
import pygame
import sys


# RED=(255,0,0)
# WHITE=(255,255,255)

def minimax(board,depth,isComputer=True,visualize=False,game=None,alpha=-float("inf"),beta=float("inf")):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    if depth==0 or board.winner():
        return board.evaluate(),board
    if isComputer:
        bestScore=float('-inf')
        best_move=None
        for move in get_all_moves(board,WHITE,visualize,game):
            score,_=minimax(move,depth-1,False,visualize,game,alpha,beta)
            bestScore=max(bestScore,score)
            if bestScore==score:
                best_move=move
            alpha=max(alpha,bestScore)
            if alpha>=beta:
                break
        return bestScore,best_move
    else:
        bestScore=float('inf')
        best_move=None
        for move in get_all_moves(board,RED,visualize,game):
            score,_=minimax(move,depth-1,True,visualize,game,alpha,beta)
            bestScore=min(bestScore,score)
            if bestScore==score:
                best_move=move
            beta=min(beta,bestScore)
            if beta<=alpha:
                break
        return bestScore,best_move

def get_all_moves(board,color,visualize,game):
    moves=[]
    for piece in board.get_all_pieces(color):
        valid_moves=board.get_valid_moves(piece)
        for move,skip in valid_moves.items():
            if visualize:
                draw_moves(game,board,piece)
            temp_board=deepcopy(board)
            temp_piece=temp_board.get_board_piece(piece.row,piece.col)
            new_board=simulate_move(temp_piece,move,temp_board,skip)
            moves.append(new_board)

    return moves
def draw_moves(game,board,piece):
    valid_moves=board.get_valid_moves(piece)
    board.draw(game.WIN)
    pygame.draw.circle(game.WIN,GREEN,(piece.x,piece.y),SQUARE_SIZE//2,5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    pygame.time.delay(VIS_DELAY)
def simulate_move(piece,move,board,skip):
    board.move_piece(piece,move[0],move[1])
    if skip:
        board.remove(skip)
    return board