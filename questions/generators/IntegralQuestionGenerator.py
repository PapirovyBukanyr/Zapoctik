import numpy as np
from ..Question import Question

class IntegralQuestionGenerator(Question):
    def __init__(self):
        super().__init__()
        
    def generateQuestion(self):
        """Generování náhodné otázky na určení primitivní funkce

        Returns:
            IntegralQuestionGenerator: Vrací samo sebe s vygenerovanou otázkou a odpovědí
        """
        a = np.random.randint(1, 5)
        b = np.random.randint(5, 10)
        c = np.random.randint(1, 10)
        d = np.random.randint(1, 4)
        
        self.questionText = "Urči hodnotu výrazu:"
        self.questionLatex = f"\\\\int_{{{a}}}^{{{b}}} {c}x^{d} dx"
        upperIntegralLimit = (c/(d+1))*b**(d+1)
        lowerIntegralLimit = (c/(d+1))*a**(d+1)
        self.answer = upperIntegralLimit - lowerIntegralLimit
        
        return self