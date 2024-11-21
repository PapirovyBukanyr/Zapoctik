import numpy as np
from ..Question import Question

class InfinitiveSeriesQuestionGenerator(Question):
    def generateQuestion(self):
        """Generování náhodné otázky na konvergenci nekonečných řad

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
