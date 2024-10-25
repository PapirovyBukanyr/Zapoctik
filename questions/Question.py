class Question:
    """Třída předpisu otázky
    """
    def __init__(self):
        """Konstruktor třídy Question
        """
        self.question = ""
        self.answer = ""

    def __str__(self):
        """Metoda na výpis otázky s odpovědí
        Returns:
            Vrátí otázku a odpověď ve formátu string
        """
        return f"Otázka: {self.question}\nOdpověď: {self.answer}"
    
    def checkAnswer(self, answer):
        """Metoda na kontrolu odpovědi
        
        Args:
            answer - zadaná odpověď
        Returns:
            bool, true pokud je odpověď správná
        """
        try:
            self.answer = round(self.answer).__str__()
        except:
            self.answer = self.answer.__str__()
        return answer.strip() == self.answer.strip()