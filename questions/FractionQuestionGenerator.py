import random
from Question import Question

class FractionQuestionGenerator(Question):
    def generateFraction(self):
        """Vygenerování náhodné dvojice čísel
        
        Returns:
            Tuple dvou integerů, (numerator, denominator), kde numerator je čitatel v rozmezí 10-100 a denominator jmenovatel v rozmezí 1-10
        """
        numerator = random.randint(10, 100)
        denominator = random.randint(1, 10)
        return numerator, denominator
    
    def simplifyFraction(self, numerator, denominator):
        """Zjednodušení zlomku
        
        Args:
            numerator: čitatel 
            denominator: jmenovatel
        Returns:
            Tuple dvou integerů, (numerator, denominator), kde numerator je čitatel a denominator jmenovatel zjednodušeného zlomku
        """
        gcd = self.greatestCommonDivisor(numerator, denominator)
        return numerator // gcd, denominator // gcd
    
    def greatestCommonDivisor(self, a, b):
        """Výpočet největšího společného dělitele
        
        Args:
            a: první číslo
            b: druhé číslo
        Returns:
            Největší společný dělitel
        """
        while b != 0:
            a, b = b, a % b
        return a
    
    def fractionToString(self, numerator, denominator):
        """Převedení zlomku na string
        
        Args:
            numerator: čitatel 
            denominator: jmenovatel
        Returns:
            String reprezentace zlomku
        """
        return f"\\frac{ {numerator} }{ {denominator} }"
    
    def fractionToAnswer(self, numerator, denominator):
        """Převedení zlomku na string
        
        Args:
            numerator: čitatel 
            denominator: jmenovatel
        Returns:
            String reprezentace zlomku
        """
        return f"{numerator}/{denominator}"
    
    def generateQuestion(self):
        """Vygenerování náhodné otázky na zlomky

        Returns:
            Samo sebe s vygenerovanou otázkou a odpovědí
        """
        randomQuestion = random.randint(1, 3)
        numerator, denominator = self.generateFraction()
        
        if randomQuestion == 1:
            self.question = f"Zjednodušte tento zlomek: {self.fractionToString(numerator, denominator)}"
            simplified_numerator, simplified_denominator = self.simplifyFraction(numerator, denominator)
            self.answer = self.fractionToAnswer(simplified_numerator, simplified_denominator)
        
        elif randomQuestion == 2:
            self.question = f"Jaký je nejmenší společný násobek {numerator} and {denominator}?"
            self.answer = self.greatestCommonDivisor(numerator, denominator)
        
        elif randomQuestion == 3:
            self.question = f"Odhadni výsledek {self.fractionToString(numerator, denominator)} "
            self.answer = numerator / denominator
        
        return self

if __name__ == "__main__":
    fqg = FractionQuestionGenerator()
    print(fqg.generateQuestion().__str__())