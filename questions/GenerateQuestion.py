import random as rand
from questions.Question import Question
from questions.generators.MatrixQuestionGenerator import MatrixQuestionGenerator
from questions.generators.FractionQuestionGenerator import FractionQuestionGenerator
from questions.generators.DerivativeQuestionGenerator import DerivativeQuestionGenerator
from questions.generators.LinearEquationSystemQuestionGenerator import LinearEquationSystemQuestionGenerator
from questions.generators.InfinitiveSeriesQuestionGenerator import InfinitiveSeriesQuestionGenerator
from questions.generators.IntegralQuestionGenerator import IntegralQuestionGenerator
from questions.generators.AnalyticGeometryQuestionGenerator import AnalyticGeometryQuestionGenerator


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
            string, string (questionText, questionLatex): otázka
        """
        randomQuestion = rand.randint(1, 7)
        
        if randomQuestion == 1: # Generování otázky na matice
            question = MatrixQuestionGenerator() 
            
        elif randomQuestion == 2: # Generování otázky na zlomky
            question = FractionQuestionGenerator()
            
        elif randomQuestion == 3: # Generování otázky na derivace
            question = DerivativeQuestionGenerator()
            
        elif randomQuestion == 4: # Generování otázky na soustavu lineárních rovnic
            question = LinearEquationSystemQuestionGenerator()
            
        elif randomQuestion == 5: # Generování otázky na konvergenci nekonečných řad
            question = InfinitiveSeriesQuestionGenerator()
        
        elif randomQuestion == 6: # Generování otázky na určení hodnoty integrálu
            question = IntegralQuestionGenerator()
            
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
    