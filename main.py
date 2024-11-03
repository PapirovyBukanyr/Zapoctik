# Zde se to pak celé spustí
from games import *
from questions import *

"""
Zde by měl být přehled všech funkcí, co budeš potřebovat pro frontend. 
Pokud něco chybí, nebo něco nepotřebuješ, dej mi vědět. 
Všechny vrací dvojrozměrný list objektů Field, které mají atributy color a piece.
Pokud je políčko prázdné, je to None.
Snažil jsem se o maximální sjednocení funkcí, snad to pro tebe bude snadné naprogramovat.
Marek
"""

ticTacToe = TicTacToe()
while True:
    print(ticTacToe.getBoard())
    print(ticTacToe.makeMove([int(input("zadejte radek: ")), int(input("zadejte sloupec: "))]))
    print(ticTacToe.checkEnd())
    
    if ticTacToe.checkEnd() != None:
        break
        
        
checkers = Checkers()
while True:
    print(checkers.getBoard())  
    print(checkers.choosePiece([int(input("zadejte radek: ")), int(input("zadejte sloupec: "))]))
    print(checkers.makeMove([int(input("zadejte radek: ")), int(input("zadejte sloupec: "))]))
    if checkers.checkEnd() != None:
        break
        
        
chess = Chess()
while True:
    print(chess.getBoard())
    print(chess.choosePiece([int(input("zadejte radek: ")), int(input("zadejte sloupec: "))]))
    print(chess.makeMove([int(input("zadejte radek: ")), int(input("zadejte sloupec: "))]))
    print(chess.promote("Q"))
    if chess.checkEnd() != None:
        break


qg = GenerateQuestion()
while True:
    qg.generateQuestion() # automaticky vypíše otázku i s odpovědí do terminálu, nechal bych to kvůli debugování, klidně to odstraním. Marek
    print("Odpověď: "+qg.doupovcuvOperator()) 
    if qg.checkAnswer(input("Zadej odpověď: ")):
        print("Správně")
    else:
        print("Špatně")