import random as rand
import sympy as sp
from IPython.display import display,Latex
from Question import Question
from generators.MatrixQuestionGenerator import MatrixQuestionGenerator
from generators.FractionQuestionGenerator import FractionQuestionGenerator
from generators.DerivativeQuestionGenerator import DerivativeQuestionGenerator
from generators.LinearEquationSystemQuestionGenerator import LinearEquationSystemQuestionGenerator

class GenerateQuestion (Question):
    """Třída na generování otázek
    Pro generování otázek použij metodu generateQuestion
    Pro kontrolu odpovědí použij metodu checkAnswer s parametrem answer
    Výsledky se zaokrouhlují na celá čísla!!!
    """
    def __init__(self):
        """Konstruktor třídy GenerateQuestion
        """
        super().__init__()
        print("Otázky jsou připraveny ke generování")
        
    def generateQuestion(self):
        """Metoda na generování otázek
        
        Returns:
            otázka ve formátu string
        """
        randomQuestion = rand.randint(1, 4)
        
        if randomQuestion == 1: # Generování otázky na matice
            question = MatrixQuestionGenerator() 
            
        elif randomQuestion == 2: # Generování otázky na zlomky
            question = FractionQuestionGenerator()
            
        elif randomQuestion == 3: # Generování otázky na derivace
            question = DerivativeQuestionGenerator()
            
        else: # Generování otázky na soustavu lineárních rovnic
            question = LinearEquationSystemQuestionGenerator()
            
        
        question.generateQuestion()
        self.answer = question.answer
        self.question = question.question
            
        print(self)
        
        return self.question
    
if __name__ == "__main__":
    gq = GenerateQuestion()
    while True:
        gq.generateQuestion()
        if gq.checkAnswer(input("Zadej odpověď: ")):
            print("Odpověď je správná")
        else:
            print("Odpověď je špatná")
        print("Další otázka")
    