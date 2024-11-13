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
        