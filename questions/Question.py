class Question:
    """Třída předpisu otázky
    """
    def __init__(self):
        """Konstruktor třídy Question
        """
        self.questionText = ""
        self.questionLatex = ""
        self.answer = ""

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
        return answer.strip() == self.answer.strip()
    
    def doupovcuvOperator(self):
        """Metoda na získání odpovědi

        Returns:
            string: odpověď
        """
        return self.answer.__str__()
    
    def generateQuestion(self):
        """Funkce na generování otázky

        Returns:
            string, string: Vrací otázku
        """
        raise NotImplementedError