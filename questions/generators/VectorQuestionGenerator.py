from ..Question import Question
import random
import numpy as np

class VectorQuestionGenerator(Question):
    """Generátor otázek na vektory
    """
    
    def __init__(self):
        """Konstruktor třídy otázek na množiny
        """
        super().__init__()
        self.time = 30
        self.numberOfQuestions = 4
        
    
    def generateVector(self, n = None):
        """Generování vektoru
        """
        if n is None or n not in range(1, 4):
            n = random.randint(1, 3)
            
        vector = np.zeros(n)
        vector = np.random.randint(-3, 3, n)
        
        return vector
    
    
    def calculateVectorLength(self, vector):
        """Výpočet délky vektoru
        """
        return abs(np.linalg.norm(vector))
    
    
    def vectorToLatex(self, vector):
        """Převod vektoru na LaTeX
        """
        vectorString = ""
        
        for i in range(len(vector)):
            if i == 0:
                vectorString += f"{vector[i]}"
                
            else:
                vectorString += f"\\\\\\\\ {vector[i]}"
        
        return f"\\\\begin{{pmatrix}} {vectorString} \\\\end{{pmatrix}}"
    
    
    def generateQuestion(self, n = None):
        """Generování náhodné otázky na vektory
        
        Args:
            n (int): Číslo otázky, defaultně náhodné
            
        Returns:
            VectorQuestionGenerator: Vrací samo sebe s vygenerovanou otázkou a odpovědí
        """
        if n is None or n not in range(0, 4):
            randomQuestion = random.randint(0, 3)
            
        else:
            randomQuestion = n
            
        vectorDimension = random.randint(2, 3)
        firstVector = self.generateVector(vectorDimension)
        secondVector = self.generateVector(vectorDimension)
        thirdVector = self.generateVector(vectorDimension)
            
        if randomQuestion == 0:
            
            self.questionText = "Urči absolutní velikost součtu vektorů a,b,c:"
            self.questionLatex = f"\\\\vec{{a}} = {self.vectorToLatex(firstVector)} \\\\quad \\\\vec{{b}} = {self.vectorToLatex(secondVector)} \\\\quad \\\\vec{{c}} = {self.vectorToLatex(thirdVector)}"
            self.answer = self.calculateVectorLength(firstVector + secondVector + thirdVector)
        
        elif randomQuestion == 1:
            self.questionText = "Urči absolutní velikost vektorového součinu vektorů:"
            self.questionLatex = f" {self.vectorToLatex(firstVector)} \\\\times {self.vectorToLatex(secondVector)}"
            self.answer = self.calculateVectorLength(np.cross(firstVector, secondVector))
            
        elif randomQuestion == 2:
            self.questionText = "Urči absolutní velikost skalárního součinu vektorů:"
            self.questionLatex = f" {self.vectorToLatex(firstVector)} \\\\cdot {self.vectorToLatex(secondVector)}"
            self.answer = self.calculateVectorLength(np.dot(firstVector, secondVector))
            
        elif randomQuestion == 3:
            self.questionText = "Urči absolutní velikost vektoru a:"
            self.questionLatex = f"\\\\vec{{a}} = {self.vectorToLatex(firstVector)}"
            self.answer = self.calculateVectorLength(firstVector)
            
        else:
            raise ValueError("Otázka mimo index")
        
        return self