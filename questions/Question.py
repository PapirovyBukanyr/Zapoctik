from abc import ABC, abstractmethod
import numpy as np

class Question (ABC):
    """Třída předpisu otázky
    """
    
    
    def __init__(self):
        """Konstruktor třídy Question
        """
        self.questionText = "" 
        """Text otázky, nesmí obsahovat LaTeX"""
        
        self.questionLatex = "" 
        """LaTeX otázky na zobrazení"""
        
        self.answer = ""
        """Odpověď na otázku, při kontrole se zaokrouhluje na celá čísla"""
        
        self.numberOfQuestions = 0
        """Počet otázek"""
        
        self.time = 60 
        """Časový limit na otázku v sekundách"""
        
        self.hoderovaDanger = False 
        """Otázka je Hoderova danger"""


    def __str__(self):
        """Metoda na výpis otázky s odpovědí
        
        Returns:
            string: Vrátí otázku a odpověď 
        """
        return f"Otázka: {self.questionText}\n{self.questionLatex}\nOdpověď: {self.answer}"
    
    
    def checkAnswer(self, answer):
        """Metoda na kontrolu odpovědi
        
        Args:
            string: answer - zadaná odpověď
            
        Returns:
            bool: true pokud je odpověď správná
        """
        try:
            self.answer = int(np.round(self.answer)).__str__()
            
        except:
            self.answer = self.answer.__str__()
            
        return answer.strip().lower() == self.answer.strip().lower()
    
    
    def doupovcuvOperator(self):
        """Metoda na získání odpovědi

        Returns:
            string: odpověď
        """
        try:
            answer = int(np.round(self.answer)).__str__()
            
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