from ..Question import Question
import random

class RegularLanguageQuestionGenerator(Question):
    """Generátor otázek na regulární jazyky
    """
    
    
    def __init__(self):
        """Konstruktor třídy regulárních jazyků
        """
        super().__init__()
        self.numberOfQuestions = 5
    
    
    def generateQuestion(self, n = None):
        """Generování náhodné otázky na regulární jazyky

        Args:
            n (int): Číslo otázky, defaultně náhodné

        Returns:
            RegularLanguageQuestionGenerator: Vrací samo sebe s vygenerovanou otázkou a odpovědí
        """
        if n is not None and n in range(0, 5):
            randomQuestion = n
        else:
            randomQuestion = random.randint(0, 4)
            
        self.questionText = "Je následující jazyk regulární odpověď zadej ve formátu ano/ne?"
        
        if randomQuestion == 0:
            self.questionLatex = "L = \\\\{a^n | n \\\\geq 0\\\\}"
            self.answer = "ano"
            
        elif randomQuestion == 1:
            self.questionLatex = "L = \\\\{a^nb^n | n \\\\geq 0\\\\}"
            self.answer = "ne"
            
        elif randomQuestion == 2:
            self.questionLatex = "L = \\\\{a^nb^n | n \\\\leq 5\\\\}"
            self.answer = "ano"
            
        elif randomQuestion == 3:
            self.questionLatex = "L = \\\\{a^n | n \\\\leq 86 000\\\\}"
            self.answer = "ano"
            
        else:
            self.questionLatex = "L = \\\\{\\\\{a,b\\\\}^* | #_a \\\\mod7 = #_b \\\\mod12 \\\\}"
            self.answer = "ano"
        
        return self