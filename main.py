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

#game = TicTacToe()
game = Checkers()
#game = Chess()  

while game.checkEnd() == None:
    print(game.getBoard())
    
    moves = []
    
    if isinstance(game, Chess) or isinstance(game, Checkers):
        moves = game.choosePiece([int(input("zadejte radek: ")), int(input("zadejte sloupec: "))])
        print(moves)
        
    while moves != True and moves != "Promote":
        moves = game.makeMove([int(input("zadejte radek: ")), int(input("zadejte sloupec: "))])
        print(moves)
    
    if moves == "Promote":
        print(game.promote("Q"))
        
    print(game.checkEnd())
        
print (game.checkEnd())


qg = GenerateQuestion()
while True:
    qg.generateQuestion() # automaticky vypíše otázku i s odpovědí do terminálu, nechal bych to kvůli debugování, klidně to odstraním. Marek
    print("Odpověď: "+qg.doupovcuvOperator()) 
    if qg.checkAnswer(input("Zadej odpověď: ")):
        print("Správně")
    else:
        print("Špatně")