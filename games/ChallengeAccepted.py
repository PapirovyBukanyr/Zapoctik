import random; from .Enums import *; 
class ChallengeAccepted: 
    __init__=lambda s: [setattr(s, '__board', [[None for _ in range(8)] for _ in range(8)]), setattr(s, '__found', False), setattr(s, '__position', [random.randint(0, 7), random.randint(0, 7)])]; 
    __str__=lambda s: "Hledání krtka"; 
    getBoard=lambda s, color: [[Field((Colors.BLACK, Figures.SHADOW)) if color == Colors.BLACK else (Field(Colors.WHITE, Figures.PAWN) if x == s.__position[0] and y == s.__position[1] else None) for x in range(8)] for y in range(8)]; 
    choosePiece=lambda s, color: [[s.__position[0] + dx, s.__position[1] + dy] for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)] if 0 <= s.__position[0] + dx < 8 and 0 <= s.__position[1] + dy < 8] if color == Colors.WHITE else [[0, 0]]; 
    makeMove=lambda s, npos, color: [setattr(s, '__position', npos), True] if color == Colors.WHITE and npos in s.choosePiece(Colors.WHITE) else [s.__endGame(), True] if color == Colors.BLACK and s.__position == npos else False; 
    __endGame=lambda s: setattr(s, '__found', True); 
    checkEnd=lambda s: None if not s.__found else f"{Colors.BLACK} won"