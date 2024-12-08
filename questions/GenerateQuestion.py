import random as rand
from .Question import Question
from .generators import *
from .listOfQuestions import listOfQuestions


class GenerateQuestion (Question):
    """Třída na generování otázek
    Pro generování otázek použij metodu generateQuestion
    Pro kontrolu odpovědí použij metodu checkAnswer s parametrem answer
    Pro získání správné odpovědi použij funkci doupovcuvOperator
    Výsledky se zaokrouhlují na celá čísla!!!
    """
    
    
    def __init__(self):
        """Konstruktor třídy GenerateQuestion
        """
        super().__init__()
        self.numberOfQuestions = listOfQuestions
        
        
    def generateQuestion(self, n = None):	
        """Metoda na generování otázek
        
        Args: 
            n (int): Číslo otázky, defaultně náhodné
        
        Returns:
            string, string (questionText, questionLatex): otázka
        """
        if n is not None and n in range(0, len(listOfQuestions)):
            randomQuestion = n
        else:
            randomQuestion = rand.randint(0, len(listOfQuestions) - 1)
        
        question_tuple = listOfQuestions[randomQuestion]
        question = question_tuple[1]()
            
        question.generateQuestion()
        self.answer = question.answer
        self.questionText = question.questionText
        self.questionLatex = question.questionLatex
        self.hoderovaDanger = question.hoderovaDanger
        
        return self
    
    
if __name__ == "__main__":
    gq = GenerateQuestion()
    while True:
        gq.generateQuestion()
        if gq.checkAnswer(input("Zadej odpověď: ")):
            print("Odpověď je správná")
        else:
            print("Odpověď je špatná")
        print("Další otázka")
    