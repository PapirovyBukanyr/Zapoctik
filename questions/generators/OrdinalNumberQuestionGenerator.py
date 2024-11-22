import numpy as np
import sympy as sp
import random
from ..Question import Question

class OrdinalNumberQuestionGenerator(Question):
    """Generátor otázek na ordinální čísla
    """
    
    
    numberOfQuestions = 3
    """int: Počet otázek, které generátor vygeneruje
    """
    
    
    def generateQuestion(self, n = None):
        """Generování náhodné otázky na uspořádaná čísla

        Args:
            n (int): Číslo otázky, defaultně náhodné

        Returns:
            OrdinalNumberQuestionGenerator: Vrací samo sebe s vygenerovanou otázkou a odpovědí
        """
        if n is not None and n in range(0, 4):
            randomQuestion = n
        else:
            randomQuestion = random.randint(0, 3)
            
        a = 0
        b = 0
        while a != 3 and b != 3:
            a = random.randint(1, 3)
            b = random.randint(1, 3)
        if a == 3:
            a = "\\omega"
        if b == 3:
            b = "\\omega"
        
        if randomQuestion == 0:
            self.questionText = "Urči hodnotu výrazu ordinálních čísel, odpověď zadej ve formátu \"wa+b\", \"wa\", \"w+b\" nebo \"b\":"
            self.questionLatex = f"{a} + {b}"
            if a == "\\omega" and b == "\\omega":
                self.answer = "w2"
            elif a == "\\omega":
                self.answer = f"w+{b}:"
            elif b == "\\omega":
                self.answer = "w"
            else:
                self.answer = a + b
                
        elif randomQuestion == 1:
            self.questionText = "Urči hodnotu výrazu ordinálních čísel, odpověď zadej ve formátu \"w^2\",\"wa+b\", \"wa\", \"w+b\" nebo \"b\":"
            self.questionLatex = f"{a} \\cdot {b}"
            if a == "\\omega" and b == "\\omega":
                self.answer = "w^2"
            elif a == "\\omega":
                self.answer = f"w2"
            elif b == "\\omega":
                self.answer = f"w"
            else:
                self.answer = a * b
        
        elif randomQuestion == 2:
            self.questionText = "Urči hodnotu výrazu ordinálních čísel, odpověď zadej ve formátu \"w^a\",\"wa+b\", \"wa\", \"w+b\" nebo \"b\":"
            self.questionLatex = f"{a} ^ {b}"
            if a == "\\omega" and b == "\\omega":
                self.answer = "w^w"
            elif a == "\\omega":
                self.answer = f"w^{b}"
            elif b == "\\omega":
                self.answer = f"w"
            else:
                self.answer = a ** b
                
        return self
    