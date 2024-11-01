class Checkers:
    def __init__(self):
        self.board = self.create_initial_board()
        self.current_player = 'B'  # B for Black, W for White
    
    def __str__(self):
        return '\n'.join(['.'.join(row) for row in self.board])
    
    def create_initial_board(self):
        """Create an 8x8 board with the initial checkers setup."""
        board = [['' for _ in range(8)] for _ in range(8)]
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    board[row][col] = 'B'
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    board[row][col] = 'W'
        return board
    
    def playedPiecePosition(self, position, color = None):
        if color is None:
            color = self.current_player
        if self.board[position[0]][position[1]] == color:
            self.playedPiece = position
            return self.posibleMoves(position)
        return []
    
    def make_move(self, end_row, end_col):
        """Make a move on the board. Return a message indicating whether the move was successful."""
        if self.is_valid_move(self.playedPiece[0], self.playedPiece[1], end_row, end_col):
            self.board[end_row][end_col] = self.board[self.playedPiece[0]][self.playedPiece[1]]
            self.board[self.playedPiece[0]][self.playedPiece[1]] = ''
            if abs(end_row - self.playedPiece[0]) == 2:
                self.board[(self.playedPiece[0] + end_row) // 2][(self.playedPiece[1] + end_col) // 2] = ''
            self.current_player = 'B' if self.current_player == 'W' else 'W'
            return "Move made"
        else:
            return "Invalid move"
    
    def is_valid_move(self, start_row, start_col, end_row, end_col):
        if self.board[start_row][start_col] != self.current_player:
            return False
        if self.board[end_row][end_col] != '':
            return False
        if abs(end_row - start_row) == 1 and abs(end_col - start_col) == 1:
            return True
        if abs(end_row - start_row) == 2 and abs(end_col - start_col) == 2:
            if self.board[(start_row + end_row) // 2][(start_col + end_col) // 2] not in ('', self.current_player):
                return True
        return False
    
    def posibleMoves(self, position):
        moves = []
        for row in range(8):
            for col in range(8):
                if self.is_valid_move(position[0], position[1], row, col):
                    moves.append((row, col))
        return moves
    
    def reset(self):
        self.board = self.create_initial_board()
        self.current_player = 'B'