import numpy as np
from ..Question import Question

class InfinitiveSeriesQuestionGenerator(Question):
    """Generátor otázek na konvergenci nekonečných řad
    """
    
    
    numberOfQuestions = 1
    """int: Počet otázek, které generátor vygeneruje
    """
    
    
    def __init__(self):
        """Konstruktor třídy nekonečných řad
        """
        super().__init__()
        self.time = 10
    
    
    def generateQuestion(self, n = None):	
        """Generování náhodné otázky na konvergenci nekonečných řad
        
        Args:
            n (int): Číslo otázky, defaultně náhodné

        Returns:
            InfinitiveSeriesQuestionGenerator: Vrací samo sebe s vygenerovanou otázkou a odpovědí
        """
        a = np.random.randint(1, 10)
        b = np.random.randint(1, 10)
        
        self.questionText = "Urči konvergenci nekonečné řady, odpověď zadej ve formátu konverguje/diverguje:"
        self.questionLatex = f"\\\\sum_{{n=1}}^\\\\infty \\\\left(\\\\frac{{{a}}}{{{b}}}\\\\right)^n"
        
        if a/b < 1:
            self.answer = "konverguje"
            
        else:
            self.answer = "diverguje"
        
        return self 
