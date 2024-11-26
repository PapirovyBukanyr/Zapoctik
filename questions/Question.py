from abc import ABC, abstractmethod

class Question (ABC):
    """Třída předpisu otázky
    """
    
    
    def __init__(self):
        """Konstruktor třídy Question
        """
        self.questionText = ""
        self.questionLatex = ""
        self.answer = ""
        self.numberOfQuestions = 0
        self.time = 60
        self.hoderovaDanger = False

    def __str__(self):
        """Metoda na výpis otázky s odpovědí
        
        Returns:
            string: Vrátí otázku a odpověď 
        """
        return f"Otázka: {self.questionText}{self.questionLatex}\nOdpověď: {self.answer}"
    
    
    def checkAnswer(self, answer):
        """Metoda na kontrolu odpovědi
        
        Args:
            string: answer - zadaná odpověď
            
        Returns:
            bool: true pokud je odpověď správná
        """
        try:
            self.answer = round(self.answer).__str__()
            
        except:
            self.answer = self.answer.__str__()
            
        return answer.strip().lower() == self.answer.strip().lower()
    
    
    def doupovcuvOperator(self):
        """Metoda na získání odpovědi

        Returns:
            string: odpověď
        """
        try:
            answer = round(self.answer).__str__()
            
        except:
            answer = self.answer.__str__()
            
        return answer
    
    
    @abstractmethod
    def generateQuestion(self, n = None):	
        """Funkce na generování otázky

        Returns:
            string, string: Vrací otázku
        """
        pass