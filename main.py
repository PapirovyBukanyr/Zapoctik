# Zde se to pak celé spustí
from games import *
from questions import *

"""
ticTacToe = TicTacToe()
while True:
    print(ticTacToe.getBoard())
    print(ticTacToe.makeMove(int(input("zadejte radek: ")), int(input("zadejte sloupec: "))))
    if ticTacToe.checkEnd() != None:
        break

checkers = Checkers()
while True:
    print(checkers)
    print(checkers.playedPiecePosition([int(input("zadejte radek: ")), int(input("zadejte sloupec: "))], "B"))
    print(checkers.make_move(int(input("zadejte radek: ")), int(input("zadejte sloupec: "))))
    if checkers.checkEnd() != None:
        break
        
        """
game = Chess()
qg = GenerateQuestion()

#ukazka prace s backendem
while True:
    print(game.choosePiece([int(input("zadejte radek: ")), int(input("zadejte sloupec: "))]))
    print(game.makeMove([int(input("zadejte radek: ")), int(input("zadejte sloupec: "))]))
    print(game.promote("Q"))
    print(game.getBoard())

    qg.generateQuestion() # automaticky vypíše otázku i s odpovědí do terminálu, nechal bych to kvůli debugování, klidně to odstraním. Marek
    print("Odpověď: "+qg.doupovcuvOperator()) 
    if qg.checkAnswer(input("Zadej odpověď: ")):
        print("Správně")
    else:
        print("Špatně")