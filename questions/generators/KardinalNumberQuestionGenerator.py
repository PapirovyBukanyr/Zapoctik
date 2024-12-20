import numpy as np
import sympy as sp
import random
from ..Question import Question

class KardinalNumberQuestionGenerator(Question):
    """Generátor otázek na kardinální čísla
    """
    
    
    def __init__(self):
        """Konstruktor třídy otázek na kardinální čísla
        """
        super().__init__()
        self.time = 10
        self.numberOfQuestions = 2
    
    
    def generateQuestion(self, n = None):	
        """Generování náhodné otázky na kardinální čísla

        Args:
            n (int): Číslo otázky, defaultně náhodné
            
        Returns:
            KardinalNumberQuestionGenerator: Vrací samo sebe s vygenerovanou otázkou a odpovědí
        """
        if n is not None and n in range(1, 3):
            randomQuestion = n
            
        else:
            randomQuestion = random.randint(0, 1)
        
        a = 0
        b = 0
        # NEODVOLÁM A NEPŘEPÍŠU!!!
        while a != 4 and b != 4 and a != 3 and b != 3:
            a = random.randint(2, 4)
            b = random.randint(2, 4)
            
        if a == 3 or a == 4:
            a = a%2
            a = f"\\\\aleph_{a}"
            
        if b == 3 or b == 4:
            b = b%2
            b = f"\\\\aleph_{b}"
        
        if randomQuestion == 0:
            self.questionText = "Urči mohutnost výrazu kardinálních čísel, odpověď zadej ve formátu \"1\"/\"N\"/\"R\"/\"V\" (kardinalita přirozených čísel/reálných čísel/větší):"
            self.questionLatex = f"{a} \\\\times {b}"
            
            if a == "\\\\aleph_0" and b == "\\\\aleph_0":
                self.answer = "N"
                
            elif a == "\\\\aleph_0" and b == 2:
                self.answer = "N"
                
            elif a == 2 and b == "\\\\aleph_0":
                self.answer = "N"
                
            elif a == "\\\\aleph_1" and b == "\\\\aleph_1":
                self.answer = "R"
                
            elif a == "\\\\aleph_1" and b == 2:
                self.answer = "R"
                
            elif a == 2 and b == "\\\\aleph_1":
                self.answer = "R"
                
            elif a == "\\\\aleph_0" and b == "\\\\aleph_1":
                self.answer = "R"
                
            elif a == "\\\\aleph_1" and b == "\\\\aleph_0":
                self.answer = "R"  
                          
            else:
                self.answer = 1
        
        elif randomQuestion == 1:
            self.questionText = "Urči mohutnost výrazu kardinálních čísel, odpověď zadej ve formátu \"1\"/\"N\"/\"R\"/\"V\" (kardinalita přirozených čísel/reálných čísel/větší):"
            self.questionLatex = f"{a} ^ {{{b}}}"
            
            if a == "\\\\aleph_0" and b == "\\\\aleph_0":
                self.answer = "R"
                
            elif a == "\\\\aleph_0" and b == 2:
                self.answer = "N"
                
            elif a == 2 and b == "\\\\aleph_0":
                self.answer = "R"
                
            elif a == "\\\\aleph_1" and b == "\\\\aleph_1":
                self.answer = "V"
                
            elif a == "\\\\aleph_1" and b == 2:
                self.answer = "R"
                
            elif a == 2 and b == "\\\\aleph_1":
                self.answer = "V"
                
            elif a == "\\\\aleph_0" and b == "\\\\aleph_1":
                self.answer = "V"
                
            elif a == "\\\\aleph_1" and b == "\\\\aleph_0":
                self.answer = "R"
            
            else:
                self.answer = 1
            
        return self