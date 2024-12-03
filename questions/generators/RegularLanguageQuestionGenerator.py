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
        
        limit = random.randint(0, 86000)
        
        if randomQuestion == 0:
            self.questionLatex = f"L = \\\\{{a^n | n \\\\geq {limit}\\\\}}"
            self.answer = "ano"
            
        elif randomQuestion == 1:
            self.questionLatex = f"L = \\\\{{a^nb^n | n \\\\geq {limit}\\\\}}"
            self.answer = "ne"
            
        elif randomQuestion == 2:
            self.questionLatex = f"L = \\\\{{a^nb^n | n \\\\leq {limit}\\\\}}"
            self.answer = "ano"
            
        elif randomQuestion == 3:
            self.questionLatex = f"L = \\\\{{a^nb | n \\\\geq {limit}\\\\}}"
            self.answer = "ano"
            
        else:
            self.questionText = "Je následující jazyk regulární odpověď zadej ve formátu ano/ne? # je počet znaků"
            self.questionLatex = f"L = \\\\{{\\\\omega =\\\\{{a,b\\\\}}^* | \\\\#_a (\\\\omega)\\\\mod 7 = \\\\#_b(\\\\omega) \\\\mod {limit}\\\\}}"
            self.answer = "ano"
        
        return self