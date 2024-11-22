import random as rand
from .Question import Question
from .generators import *


class GenerateQuestion (Question):
    """Třída na generování otázek
    Pro generování otázek použij metodu generateQuestion
    Pro kontrolu odpovědí použij metodu checkAnswer s parametrem answer
    Výsledky se zaokrouhlují na celá čísla!!!
    """
    
    
    numberOfQuestions = 10
    """int: Počet otázek, které generátor vygeneruje    
    """
    
    
    def __init__(self):
        """Konstruktor třídy GenerateQuestion
        """
        super().__init__()
        print("Otázky jsou připraveny ke generování")
        
        
    def generateQuestion(self, n = None):	
        """Metoda na generování otázek
        
        Args: 
            n (int): Číslo otázky, defaultně náhodné
        
        Returns:
            string, string (questionText, questionLatex): otázka
        """
        if n is not None and n in range(0, self.numberOfQuestions):
            randomQuestion = n
        else:
            randomQuestion = rand.randint(0, 9)
        
        if randomQuestion == 0: # Generování otázky na matice
            question = MatrixQuestionGenerator() 
            
        elif randomQuestion == 1: # Generování otázky na zlomky
            question = FractionQuestionGenerator()
            
        elif randomQuestion == 2: # Generování otázky na derivace
            question = DerivativeQuestionGenerator()
            
        elif randomQuestion == 3: # Generování otázky na soustavu lineárních rovnic
            question = LinearEquationSystemQuestionGenerator()
            
        elif randomQuestion == 4: # Generování otázky na konvergenci nekonečných řad
            question = InfinitiveSeriesQuestionGenerator()
        
        elif randomQuestion == 5: # Generování otázky na určení hodnoty integrálu
            question = IntegralQuestionGenerator()
            
        elif randomQuestion == 6: # Generování otázky na množiny
            question = SetQuestionGenerator()    
            
        elif randomQuestion == 7: # Generování otázky na ordinální čísla
            question = OrdinalNumberQuestionGenerator()
            
        elif randomQuestion == 8: # Generování otázky na kardinální čísla
            question = KardinalNumberQuestionGenerator()
            
        else: # Generování otázky na analytickou geometrii
            question = AnalyticGeometryQuestionGenerator()
            
        question.generateQuestion()
        self.answer = question.answer
        self.questionText = question.questionText
        self.questionLatex = question.questionLatex
            
        print(self)
        
        return self.questionText, self.questionLatex
    
    
if __name__ == "__main__":
    gq = GenerateQuestion()
    while True:
        gq.generateQuestion()
        if gq.checkAnswer(input("Zadej odpověď: ")):
            print("Odpověď je správná")
        else:
            print("Odpověď je špatná")
        print("Další otázka")
    