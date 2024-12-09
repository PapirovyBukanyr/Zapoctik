from ..Question import Question
import random
import numpy as np


class ComplexQuestionGenerator(Question):
    """Generátor otázek na komplexní čísla
    """
    
    
    def __init__(self):
        """Konstruktor třídy komplexních čísel
        """
        super().__init__()
        self.time = 20
        self.numberOfQuestions = 5
        
        
    def generateComplexNumber(self):
        """Generování komplexního čísla
        """
        real = random.randint(-3, 3)
        imaginary = random.randint(-3, 3)
        
        return complex(real, imaginary)
    
    
    def complexNumberToLatex(self, number):
        """Převod komplexního čísla na LaTeX
        """
        if number.imag == 0:
            return f"{round(number.real)}"
        
        if number.real == 0:
            return f"{round(number.imag)}i"
        
        if number.imag < 0:
            return f"{round(number.real)}{round(number.imag)}i"
        
        return f"{round(number.real)}+{round(number.imag)}i"
    
    
    def absoluteValue(self, number):
        """Výpočet absolutní hodnoty komplexního čísla
        """
        return round(np.sqrt(number.real**2 + number.imag**2))
    
    
    def generateQuestion(self, n = None):
        """Generování náhodné otázky na komplexní čísla
        """
        if n is None or n not in range(0, 5):
            randomQuestion = random.randint(0, 4)
            
        else :
            randomQuestion = n
            
        complexNumber = self.generateComplexNumber()
        
        if randomQuestion == 0:
            self.questionText = f"Vypočtěte absolutní hodnotu komplexního čísla:"
            self.questionLatex = f"{self.complexNumberToLatex(complexNumber)}"
            self.answer = self.absoluteValue(complexNumber)
            
        elif randomQuestion == 1:
            self.questionText = f"Určete reálnou část komplexního čísla:"
            self.questionLatex = f"{self.complexNumberToLatex(complexNumber)}"
            self.answer = round(complexNumber.real)
            
        elif randomQuestion == 2:
            self.questionText = f"Určete imaginární část komplexního čísla:"
            self.questionLatex = f"{self.complexNumberToLatex(complexNumber)}"
            self.answer = round(complexNumber.imag)
            
        elif randomQuestion == 3:
            self.questionText = f"Určete komplexně sdružené komplexní číslo k číslu (odpověď zadejte ve tvaru a+bi, a, bi):"
            self.questionLatex = f"{self.complexNumberToLatex(complexNumber)}"
            self.answer = self.complexNumberToLatex(complexNumber.conjugate())
            
        elif randomQuestion == 4:
            self.questionText = f"Určete hodnotu výrazu:"
            self.questionLatex = f"({self.complexNumberToLatex(complexNumber)})\\\\cdot({self.complexNumberToLatex(complexNumber.conjugate())})"
            self.answer = round(complexNumber.real**2 + complexNumber.imag**2)
        
        return self