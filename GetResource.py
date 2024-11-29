from games.Enums import *

class GetResource:
    """Třída GetResource slouží k získání cesty k obrázku, který reprezentuje daný zdroj.
    """
    
    @staticmethod   
    def getResource(resource):
        """ Metoda na základě zadaného zdroje vrátí cestu k obrázku, který reprezentuje daný zdroj.
        
        Args:
            resource (str): Zdroj, pro který chceme získat cestu k obrázku.

        Returns:
            str: cesta k obrázku, který reprezentuje zadaný zdroj.
        """
        figure = resource.piece
        color = resource.color
        
        match(figure):
            case Figures.PAWN:
                match(color):
                    case Colors.WHITE:
                        return "resources//pawnW.png"
                    
                    case Colors.BLACK:
                        return "resources//pawnB.png"
                    
                    case Colors.RED:
                        return "resources//pawnR.png"
                    
                    case Colors.GREEN:
                        return "resources//pawnG.png"
            
            case Figures.ROOK:
                match(color):
                    case Colors.WHITE:
                        return "resources//rookW.png"
            
                    case Colors.BLACK:
                        return "resources//rookB.png"
            
            case Figures.BISHOP:
                match(color):
                    case Colors.WHITE:
                        return "resources//bishopW.png"
            
                    case Colors.BLACK:
                        return "resources//bishopB.png"
            
            case Figures.KNIGHT:
                match(color):
                    case Colors.WHITE:
                        return "resources//horseW.png"
            
                    case Colors.BLACK:
                        return "resources//horseB.png"
            
            case Figures.QUEEN:
                match(color):
                    case Colors.WHITE:
                        return "resources//queenW.png"
            
                    case Colors.BLACK:
                        return "resources//queenB.png"
            
            case Figures.KING:
                match(color):
                    case Colors.WHITE:
                        return "resources//kingW.png"
            
                    case Colors.BLACK:
                        return "resources//kingB.png"
            
            case Figures.X:
                return "resources//x.png"
            
            case Figures.O:
                return "resources//o.png"
            
            case Figures.FLAG:
                return "resources//flag.png"
            
            case Figures.EXPLOSION:
                return "resources//explosion.png"
            
            case Figures.ONE:
                return "resources//one.png"
            
            case Figures.TWO:
                return "resources//two.png"
            
            case Figures.THREE:
                return "resources//three.png"
            
            case Figures.FOUR:
                return "resources//four.png"
            
            case Figures.FIVE:
                return "resources//five.png"
            
            case Figures.SIX:
                return "resources//six.png"
            
            case Figures.SEVEN:
                return "resources//seven.png"
            
            case Figures.EIGHT:
                return "resources//eight.png"
            
            case Figures.SHADOW:
                return "resources//blanc.png"
            
            case Figures.MINE:
                return "resources//mine.png"
            
            case Figures.MOLE:
                return "resources//mole.jpg"
                
        