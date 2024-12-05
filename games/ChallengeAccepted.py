import random; from .Enums import *;
class ChallengeAccepted: __init__=lambda s: None if None == [setattr(s,'won',None),setattr(s,'chosen',[-1,-1]), setattr(s, 'position', [random.randint(0, 7), random.randint(0, 7)]),setattr(s, 'board', [[0 if [x,y] == s.position else None for x in range(8)] for y in range(8)])] else None; getBoard=lambda s, color: [[Field(Colors.BLACK, Figures.SHADOW) if s.chosen == [-1,-1] else (s.getField(x,y) if [x, y] == s.chosen else Field(Colors.WHITE,Figures.SHADOW)) for x in range(8)] for y in range(8)]; getField=lambda s, x, y: Field(Colors.BLACK, Figures.MOLE) if s.board[x][y]==0 else (Field(Colors.BLACK,Figures.ONE) if s.board[x][y]==1 else (Field(Colors.BLACK, Figures.TWO) if s.board[x][y]==2 else (Field(Colors.BLACK, Figures.THREE) if s.board[x][y]==3 else (Field(Colors.BLACK, Figures.FOUR) if s.board[x][y]==4 else (Field(Colors.BLACK, Figures.FIVE) if s.board[x][y]==5 else (Field(Colors.BLACK, Figures.SIX) if s.board[x][y]==6 else (Field(Colors.BLACK, Figures.SEVEN) if s.board[x][y]==7 else (Field(Colors.BLACK, Figures.EIGHT) if s.board[x][y]==8 else None))))))));moveMole = lambda s: [setattr(s, 'position', random.choice([[nx, ny] for nx, ny in [(s.position[0] + 1, s.position[1]), (s.position[0] - 1, s.position[1]), (s.position[0], s.position[1] + 1), (s.position[0], s.position[1] - 1)] if 0 <= nx < 8 and 0 <= ny < 8])),setattr(s, 'board', [[0 if [x, y] == s.position else (s.board[y][x] + 1 if s.board[y][x] is not None and s.board[y][x] != 8 else None) for x in range(8)] for y in range(8)])]; makeMove=lambda s, npos, color, rightClick = False: False if rightClick or npos[0] >7 or npos[1] >7 or npos[0] <0 or npos[1] <0 else (True if None == [s.moveMole() if s.won == None else None, setattr(s, 'chosen', [npos[1],npos[0]]), setattr(s, 'won', color if s.chosen[0] == s.position[1] and s.chosen[1] == s.position[0] else None), s.printToTerminal()] else True); checkEnd=lambda s: None if None == s.won else f"{Colors.BLACK} won"; printToTerminal=lambda s: print("\n".join([" ".join([str(s.board[x][y]) for x in range(8)]) for y in range(8)]))















































"""Třída ChallengeAccepted slouží k reprezentaci hry Hledání krtka.

Attributes:
    won (Enum Colors): Barva, která vyhrála hru
    chosen (list): Pozice, kterou hráč vybral
    position (list): Pozice krtka
    board (list): Hrací plocha


Methods:
    __init__(): Konstruktor třídy
    getBoard(color): Vrací hrací plochu
    getField(x, y): Vrací pole na dané pozici
    moveMole(): Pohne krtka
    makeMove(npos, color, rightClick): Provede tah
    checkEnd(): Zkontroluje, zda hra skončila
    printToTerminal(): Vypíše hrací plochu na terminál
    
Poznámka:
    Hra vznikla na protest proti zadání, kde bylo definováno, že žádná funkce pro přehlednost nesmí být delší než 40 řádků.
    Tato hra je napsána na jeden řádek jako důkaz toho, že stručnost není ekvivalentní s přehledností.
    Nehledě na to, že mě Filip vyhecoval, abych to napsal.
    """ 
