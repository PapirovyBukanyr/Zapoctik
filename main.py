# Zde se to pak celé spustí
from chess import *

board = Board()
board.setupNormalBoard()

print(board)
board[6,1].move(board, [4,1])
print(board)
print(board[4,1].lastMoveWasDouble)
board[4,1].move(board, [3,1])
print(board)
print(board[3,1].lastMoveWasDouble)
board[1,0].move(board, [3,0])
print(board)
print(board[3,0].lastMoveWasDouble)
print(board[3,1].lastMoveWasDouble)
print(board[3,1].possibleMoves(board))