# Zde se to pak celé spustí

from chess import *

board = Board()
board.setupNormalBoard()
print(board)

board[6,4].move(board, [4,4])
print(board)
board[1,4].move(board, [3,4])
print(board)
board[7,1].move(board, [6,2])
print(board)
board[0,3].move(board, [2,5])
print(board)
board[7,3].move(board, [5,5])
print(board)
board[0,5].move(board, [3,2])
print(board)
board[6,3].move(board, [5,3])
print(board)
board[0,6].move(board, [2,7])
print(board)
board[7,2].move(board, [6,3])
print(board)
board[2,2] = Queen(Colors.WHITE, [2,2])
print(board)
print(board[0,4].possibleMoves(board))
print(board[7,4].possibleMoves(board))
print(board[1,3].possibleMoves(board))