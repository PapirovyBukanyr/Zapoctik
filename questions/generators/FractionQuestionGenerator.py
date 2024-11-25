import random
from ..Question import Question

class FractionQuestionGenerator(Question):
    """Generátor otázek na zlomky
    """
    
    
    numberOfQuestions = 5
    """int: Počet otázek, které generátor vygeneruje
    """
    
    
    def generateFraction(self):
        """Vygenerování náhodné dvojice čísel
        
        Returns:
            int, int: (numerator, denominator), kde numerator je čitatel v rozmezí 10-100 a denominator jmenovatel v rozmezí 1-10
        """
        numerator = random.randint(10, 100)
        denominator = random.randint(1, 10)
    
        return numerator, denominator
    
    
    def simplifyFraction(self, numerator, denominator):
        """Zjednodušení zlomku
        
        Args:
            numerator (int): čitatel 
            denominator (int): jmenovatel
        Returns:
            int, int: (numerator, denominator), kde numerator je čitatel a denominator jmenovatel zjednodušeného zlomku
        """
        gcd = self.greatestCommonDivisor(numerator, denominator)
        
        return numerator // gcd, denominator // gcd
    
    
    def lowestCommonMultiple(self, a, b):
        """Výpočet nejmenšího společného násobku
        
        Args:
            a (int): první číslo
            b (int): druhé číslo
        
        Returns:
            int: Nejmenší společný násobek
        """
        return a * b // self.greatestCommonDivisor(a, b)
    
    
    def greatestCommonDivisor(self, a, b):
        """Výpočet největšího společného dělitele
        
        Args:
            a (int): první číslo
            b (int): druhé číslo
        Returns:
            int: Největší společný dělitel
        """
        while b != 0:
            a, b = b, a % b
        
        return a
    
    
    def fractionToString(self, numerator, denominator):
        """Převedení zlomku na string
        
        Args:
            numerator (int): čitatel 
            denominator (int): jmenovatel
            
        Returns:
            String: reprezentace zlomku v latexu
        """
        return f"\\frac{ {numerator} }{ {denominator} }"
    
    
    def fractionToAnswer(self, a, b):
        """Převedení zlomku na string
        
        Args:
            numerator (int): čitatel 
            denominator (int): jmenovatel
            
        Returns:
            String: reprezentace zlomku ve formátu "a/b"
        """
    
        return f"{a}/{b}"
    
    
    def generateQuestion(self, n = None):
        """Vygenerování náhodné otázky na zlomky
        
        Args:
            n (int): Číslo otázky, defaultně náhodné

        Returns:
            FractionQuestionGenerator: Samo sebe s vygenerovanou otázkou a odpovědí
        """
        if n is not None and n in range(0, 5):
            randomQuestion = n
        else:
            randomQuestion = random.randint(0, 4)
    
        numerator, denominator = self.generateFraction()
        
        if randomQuestion == 0:
            self.questionText = f"Zjednodušte tento zlomek. Odpověď zadejte ve tvaru čitatel/jmenovatel"
            self.questionLatex = self.fractionToString(numerator, denominator)
            simplified_numerator, simplified_denominator = self.simplifyFraction(numerator, denominator)
            self.answer = self.fractionToAnswer(simplified_numerator, simplified_denominator)
        
        elif randomQuestion == 1:
            self.questionText = f"Jaký je největší společný dělitel {numerator} and {denominator}?"
            self.questionLatex = "\scalebox{10}{\textbf{?}}"
            self.answer = self.greatestCommonDivisor(numerator, denominator)
        
        elif randomQuestion == 2:
            self.questionText = "Odhadni výsledek zlomku "
            self.questionLatex = self.fractionToString(numerator, denominator)
            self.answer = numerator / denominator
        
        elif randomQuestion == 3:
            self.questionText = f"Jaký je zbytek po dělení {numerator} číslem {denominator}?"
            self.questionLatex = "\scalebox{10}{\textbf{?}}"
            self.answer = numerator % denominator
            
        else:
            self.questionText = f"Jaký je nejmenší společný násobek {numerator} and {denominator}?"
            self.questionLatex = "\scalebox{10}{\textbf{?}}"
            self.answer = self.lowestCommonMultiple(numerator, denominator)
        
        return self


if __name__ == "__main__":
    fqg = FractionQuestionGenerator()
    print(fqg.generateQuestion().__str__())