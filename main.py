# Zde se to pak celé spustí
from chess import *
from questions.GenerateQuestion import GenerateQuestion


game = GameController()
qg = GenerateQuestion()

#ukazka prace s backendem
while True:
    print(game.board)
    print(game.playedPiecePosition(Colors.WHITE, [int(input("zadejte radek: ")), int(input("zadejte sloupec: "))]))
    print(game.makeMove([int(input("zadejte radek: ")), int(input("zadejte sloupec: "))]))
    print(game.promote("Q"))

    qg.generateQuestion() # automaticky vypíše otázku i s odpovědí do terminálu, nechal bych to kvůli debugování, klidně to odstraním. Marek
    print("Odpověď: "+qg.doupovcuvOperator()) 
    if qg.checkAnswer(input("Zadej odpověď: ")):
        print("Správně")
    else:
        print("Špatně")
    