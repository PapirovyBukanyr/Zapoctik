import random as rand
import Question 
from Question import Question
from MatrixQuestionGenerator import MatrixQuestionGenerator
from FractionQuestionGenerator import FractionQuestionGenerator

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
        randomQuestion = rand.randint(1, 2)
        
        if randomQuestion == 1: # Generování otázky na matice
            question = MatrixQuestionGenerator() 
            
        elif randomQuestion == 2: # Generování otázky na zlomky
            question = FractionQuestionGenerator()
            
        elif randomQuestion == 3:
            """TODO"""
            
        else:
            """TODO"""
            
        
        question.generateQuestion()
        self.answer = question.answer
        self.question = question.question
            
        print(self)
        
        return self.question
    
if __name__ == "__main__":
    gq = GenerateQuestion()
    gq.generateQuestion()
    if gq.checkAnswer(input("Zadej odpověď: ")):
        print("Odpověď je správná")
    else:
        print("Odpověď je špatná")
    
    