from games.Enums import *

class GetResource:
    @staticmethod   
    def getResource(resource):
        figure = resource.piece
        color = resource.color
        match(figure):
            case Figures.PAWN:
                match(color):
                    case Colors.WHITE:
                        return "resources//pawnW.png"
                    case Colors.BLACK:
                        return "resources//pawnB.png"
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
                
        