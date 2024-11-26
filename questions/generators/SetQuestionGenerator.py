import numpy as np
import sympy as sp
import random
from ..Question import Question

class SetQuestionGenerator(Question):
    """Generátor otázek na množiny
    """
    
    
    def __init__(self):
        """Konstruktor třídy otázek na množiny
        """
        super().__init__()
        self.time = 10
        self.numberOfQuestions = 7
    
    
    def generateQuestion(self, n = None):
        """Generování náhodné otázky na množiny
        
        Args:
            n (int): Číslo otázky, defaultně náhodné

        Returns:
            SetQuestionGenerator: Vrací samo sebe s vygenerovanou otázkou a odpovědí
        """
        if n is not None and n in range(0, 7):
            randomQuestion = n
            
        else:
            randomQuestion = random.randint(0, 6)
        
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0
        
        while a == b or b == c or a == c:
            a = np.random.randint(1, 10)
            b = np.random.randint(1, 10)
            c = np.random.randint(1, 10)
       
        while d == e or e == f or d == f:
            d = np.random.randint(1, 10)
            e = np.random.randint(1, 10)
            f = np.random.randint(1, 10)
        
        if randomQuestion == 0:
            self.questionText = "Urči součet prvků sjednocení množin:"
            self.questionLatex = f"\\\\{{ {a}, {b}, {c}\\\\}} \\\\cup \\\\{{ {d}, {e}, {f}\\\\}}"
            self.answer = sum(set([a, b, c]) | set([d, e, f]))
        
        elif randomQuestion == 1:
            self.questionText = "Urči součet prvků průnik množin:"
            self.questionLatex = f"\\\\{{ {a}, {b}, {c}\\\\}} \\\\cap \\\\{{ {d}, {e}, {f}\\\\}}"
            self.answer = sum(set([a, b, c]) & set([d, e, f]))
        
        elif randomQuestion == 2:
            self.questionText = "Urči součet prvků rozdílu množin:"
            self.questionLatex = f"\\\\{{ {a}, {b}, {c}\\\\}} \\\\setminus \\\\{{ {d}, {e}, {f}\\\\}}"
            self.answer = sum(set([a, b, c]) - set([d, e, f]))
        
        elif randomQuestion == 3:
            self.questionText = "Urči součet prvků symetrické diference množin:"
            self.questionLatex = f"\\\\{{ {a}, {b}, {c}\\\\}} \\\\triangle \\\\{{ {d}, {e}, {f}\\\\}}"
            self.answer = sum(set([a, b, c]) ^ set([d, e, f]))
        
        elif randomQuestion == 4:
            self.questionText = "Urči nejmenší prvek kartézského součinu podle obou parametrů (odpověď zadej ve formátu a,b):"
            self.questionLatex = f"\\\\{{ {a}, {b}, {c}\\\\}} \\\\times \\\\{{ {d}, {e}, {f}\\\\}}"
            self.answer = min([a, b, c]).__str__()+","+min([d, e, f]).__str__()
        
        elif randomQuestion == 5:
            self.questionText = "Urči největší prvek kartézského součinu podle obou parametrů (odpověď zadej ve formátu a,b):"
            self.questionLatex = f"\\\\{{ {a}, {b}, {c}\\\\}} \\\\times \\\\{{ {d}, {e}, {f}\\\\}}"
            self.answer = max([a, b, c]).__str__()+","+max([d, e, f]).__str__()
        
        else:
            self.questionText = "Urči počet prvků kartézského součinu:"
            self.questionLatex = f"\\\\{{ {a}, {b}, {c}\\\\}} \\\\times \\\\{{ {d}, {e}, {f}\\\\}}"
            self.answer = len(set([a, b, c])) * len(set([d, e, f]))
            
        return self

if __name__ == "__main__":
    sqg = SetQuestionGenerator()
    print(sqg.generateQuestion().__str__())