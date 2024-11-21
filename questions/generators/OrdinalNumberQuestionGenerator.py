import numpy as np
import sympy as sp
import random
from ..Question import Question

class OrdinalNumberQuestionGenerator(Question):
    def generateQuestion(self):
        """Generování náhodné otázky na uspořádaná čísla

        Returns:
            OrdinalNumberQuestionGenerator: Vrací samo sebe s vygenerovanou otázkou a odpovědí
        """
        a = 0
        b = 0
        while a != 3 and b != 3:
            a = random.randint(1, 3)
            b = random.randint(1, 3)
        if a == 3:
            a = "\\\\omega"
        if b == 3:
            b = "\\\\omega"
        
        i = random.randint(0, 2)
        
        if i == 0:
            self.questionText = "Urči hodnotu výrazu ordinálních čísel, odpověď zadej ve formátu \"wa+b\", \"wa\", \"w+b\" nebo \"b\":"
            self.questionLatex = f"{a} + {b}"
            if a == "\\\\omega" and b == "\\\\omega":
                self.answer = "w2"
            elif a == "\\\\omega":
                self.answer = f"w+{b}:"
            elif b == "\\\\omega":
                self.answer = "w"
            else:
                self.answer = a + b
                
        elif i == 1:
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
        
        elif i == 2:
            self.questionText = "Urči hodnotu výrazu ordinálních čísel, odpověď zadej ve formátu \"w^a\",\"wa+b\", \"wa\", \"w+b\" nebo \"b\":"
            self.questionLatex = f"{a} ^ {b}"
            if a == "\\\\omega" and b == "\\\\omega":
                self.answer = "w^w"
            elif a == "\\\\omega":
                self.answer = f"w^{b}"
            elif b == "\\\\omega":
                self.answer = f"w"
            else:
                self.answer = a ** b
                
        return self
    