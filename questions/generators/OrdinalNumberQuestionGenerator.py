import numpy as np
import sympy as sp
import random
from ..Question import Question

class OrdinalNumberQuestionGenerator(Question):
    """Generátor otázek na ordinální čísla
    """
    
    
    def __init__(self): 
        """Konstruktor třídy otázek na ordinální čísla
        """
        super().__init__()
        self.time = 20
        self.numberOfQuestions = 3
    
    
    def generateQuestion(self, n = None):
        """Generování náhodné otázky na uspořádaná čísla

        Args:
            n (int): Číslo otázky, defaultně náhodné

        Returns:
            OrdinalNumberQuestionGenerator: Vrací samo sebe s vygenerovanou otázkou a odpovědí
        """
        if n is not None and n in range(0, 3):
            randomQuestion = n
            
        else:
            randomQuestion = random.randint(0, 2)
            
        a = 0
        b = 0
        
        while a != 3 and b != 3:
            a = random.randint(1, 3)
            b = random.randint(1, 3)
            
        if a == 3:
            a = "\\\\omega"
            
        if b == 3:
            b = "\\\\omega"
        
        if randomQuestion == 0:
            self.questionText = "Urči hodnotu výrazu ordinálních čísel, odpověď zadej ve formátu \"wa+b\", \"wa\", \"w+b\" nebo \"b\":"
            self.questionLatex = f"{a} + {b}"
            
            if a == "\\\\omega" and b == "\\\\omega":
                self.answer = "w2"
                
            elif a == "\\\\omega":
                self.answer = f"w+{b}"
                
            elif b == "\\\\omega":
                self.answer = "w"
                
            else:
                self.answer = a + b
                
        elif randomQuestion == 1:
            self.questionText = "Urči hodnotu výrazu ordinálních čísel, odpověď zadej ve formátu \"w^2\",\"wa+b\", \"wa\", \"w+b\" nebo \"b\":"
            self.questionLatex = f"{a} \\\\cdot {b}"
            
            if a == "\\\\omega" and b == "\\\\omega":
                self.answer = "w^2"
                
            elif a == "\\\\omega":
                if b == 2:
                    self.answer = "w2"
                    
                else:
                    self.answer = "w"
                    
            elif b == "\\\\omega":
                self.answer = "w"
                
            else:
                self.answer = a * b
        
        elif randomQuestion == 2:
            self.questionText = "Urči hodnotu výrazu ordinálních čísel, odpověď zadej ve formátu \"w^a\",\"wa+b\", \"wa\", \"w+b\" nebo \"b\":"
            self.questionLatex = f"{a} ^ {b}"
            
            if a == "\\\\omega" and b == "\\\\omega":
                self.answer = "w^w"
                
            elif a == "\\\\omega":
                if b == 1:
                    self.answer = "w"
                    
                else:
                    self.answer = f"w^{b}"
                
            elif b == "\\\\omega":
                if a == 1:
                    self.answer = "1"
                    
                else:
                    self.answer = f"w^{a}"
                
            else:
                self.answer = a ** b
                
        return self
    