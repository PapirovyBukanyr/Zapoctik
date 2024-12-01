from games import *
from dataclasses import dataclass

@dataclass
class Game(dataclass):
    """Třída reprezentující hru v seznamu her pro frontend
    """
    name: str
    description: str
    object: object


class ListOfGames:
    """Třída reprezentující seznam her pro frontend
    """
    
    
    @staticmethod
    def getListOfGames():
        """Vrací seznam her pro frontend
        
        Returns:
            List[Game]: seznam her
        """
        return [
                Game("Šachy",
                    "Šachy jsou strategická hra pro dva hráče. Cílem hry je vyhodit soupeřova krále. Hra končí, když je král vyhozen, případně pokud je porušeno pravidlo padesáti tahů nebo opakování pozic.",
                    Chess),
                
                Game("Piškvorky 3x3",
                    "Piškvorky jsou hra pro dva hráče. Cílem hry je spojit tři své symboly v řadě. Hra končí, když je někdo spojí nebo je plné pole.",
                    TicTacToe),
                
#                Game("Rotující piškvorky 4x4",
#                    "Rotující piškvorky jsou hra pro dva hráče. Cílem hry je spojit čtyři své symboly v řadě. Hra končí, když je někdo spojí nebo je plné pole. Do toho se hrací deska otáčí proti směru hodinových ručiček. Symboly se spojují pouze ve vertikálním a horizontálním směru.",
#                    ChessTrackGame),
                
                Game("Miny",
                    "Miny jsou hra pro dva hráče. Cílem hry je najít všechny miny a označit je vlajkou. Hra končí, když jsou všechny miny označeny, nebo když hráč najde minu. Vyhraje ten co položív více vlajek nebo neodpálí minu.",
                    Mines),
                
                Game("Šachy s mlhou války",
                    "Šachy s mlhou války jsou hra pro dva hráče. Cílem hry je vyhodit soupeřova krále. Hra končí, když je král vyhozen, případně pokud je porušeno pravidlo padesáti tahů nebo opakování pozic. Do toho je hrací deska zahalena mlhou války.",
                    ChessWithFogOfWar),
                
                Game("Dáma",
                     "Dáma je hra pro dva hráče. Cílem hry je vyhodit soupeřovy figurky. Hra končí, když jsou vyhozeny všechny soupeřovy figurky nebo soupeř již nijak nemůže táhnout.",
                     Checkers),
                
                Game("Dáma s mlhou války",
                     "Dáma s mlhou války je hra pro dva hráče. Cílem hry je vyhodit soupeřovy figurky. Hra končí, když jsou vyhozeny všechny soupeřovy figurky nebo soupeř již nijak nemůže táhnout. Do toho je hrací deska zahalena mlhou války.",
                     CheckersWithFogOfWar),
                
#                Game("Connect four",
#                     "Connect four je hra pro dva hráče. Cílem hry je spojit čtyři své symboly v řadě. Hra končí, když je někdo spojí nebo je plné pole. Symboly se spojují ve všech směrech. Symboly se přidávají od spodu.",
#                     ConnectFour),
#                
#                Game("Člověče, nezlob se!",
#                    "Člověče, nezlob se! je hra pro čtyři hráče. Cílem hry je dostat všechny své figurky do cíle. Hra končí, když někdo dostane všechny figurky do cíle.",
#                    HumanDoNotWorry),
#                
#                Game("Člověče, nezlob se! s mlhou války",
#                    "Člověče, nezlob se! s mlhou války je hra pro čtyři hráče. Cílem hry je dostat všechny své figurky do cíle. Hra končí, když někdo dostane všechny figurky do cíle. Do toho je hrací deska zahalena mlhou války.",
#                    HumanDoNotWorryWithFogOfWar),
                
                Game("Matematická hra",
                    "Matematická hra je hra pro dva hráče. Cílem hry je zodpovědět správně víc otázek než soupeř. Hra končí, když jsou všechny otázky nalezeny.",
                    MathGame),
                
                Game("Hledání krtka",
                    "Hledání krtka je hra pro dva hráče. Cílem hry je najít krtka. Hra končí, když je krtka nalezen. Ten za sebou zanechává stopu.",
                    ChallengeAccepted)                
        ]  