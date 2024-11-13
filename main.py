# Zde se to pak celé spustí
from games import *
from questions import *
from MainView import MainView
import sys
from PyQt5.QtWidgets import QApplication


print("""
_______________________________________________________________________________

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
'########::::'###::::'########:::'#######:::'######::'########:'####:'##:::'##:
..... ##::::'## ##::: ##.... ##:'##.... ##:'##... ##:... ##..::. ##:: ##::'##::
:::: ##::::'##:. ##:: ##:::: ##: ##:::: ##: ##:::..::::: ##::::: ##:: ##:'##:::
::: ##::::'##:::. ##: ########:: ##:::: ##: ##:::::::::: ##::::: ##:: #####::::
:: ##::::: #########: ##.....::: ##:::: ##: ##:::::::::: ##::::: ##:: ##. ##:::
: ##:::::: ##.... ##: ##:::::::: ##:::: ##: ##::: ##:::: ##::::: ##:: ##:. ##::
 ########: ##:::: ##: ##::::::::. #######::. ######::::: ##::::'####: ##::. ##:
........::..:::::..::..::::::::::.......::::......::::::..:::::....::..::::..::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
_______________________________________________________________________________
""")

app = QApplication(sys.argv)
window = MainView()
window.show()
sys.exit(app.exec_())

#game = TicTacToe()
#game = Checkers()
#game = Chess()  
#game = MathGame()

# while game.checkEnd() == None:
#     print(game.getBoard())
    
#     moves = []
    
#     if isinstance(game, Chess) or isinstance(game, Checkers):
#         moves = game.choosePiece([int(input("zadejte radek: ")), int(input("zadejte sloupec: "))])
#         print(moves)
#    if isinstance(game, Chess) or isinstance(game, Checkers) or isinstance(game, MathGame):
#        while moves == []:
#            moves = game.choosePiece([int(input("zadejte radek: ")), int(input("zadejte sloupec: "))])
#            print(moves)
        
#     while moves != True and moves != "Promote":
#         moves = game.makeMove([int(input("zadejte radek: ")), int(input("zadejte sloupec: "))])
#         print(moves)
    
#     if moves == "Promote":
#         print(game.promote("Q"))
        
#     print(game.checkEnd())
        
# print (game.checkEnd())

qg = GenerateQuestion()
while True:
    qg.generateQuestion() # automaticky vypíše otázku i s odpovědí do terminálu, nechal bych to kvůli debugování, klidně to odstraním. Marek
    print("Odpověď: "+qg.doupovcuvOperator()) 
    if qg.checkAnswer(input("Zadej odpověď: ")):
        print("Správně")
    else:
        print("Špatně")
