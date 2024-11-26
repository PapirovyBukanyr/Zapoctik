import numpy as np
import sympy as sp
import random
from ..Question import Question

class MatrixQuestionGenerator(Question): 
    """Generátor otázek na matice
    """  
    
    def __init__(self):
        """Konstruktor třídy matice
        """
        super().__init__()
        self.numberOfQuestions = 4
     
    
    def generateRegularMatrix(self, n = random.randint(2, 4)):
        """Generování regulární matice
        
        Args:
            n (int): Velikost matice, defaultně náhodně mezi 2 a 4

        Returns:
            numpy array int: Náhodná regulární matice
        """
        matrix = np.zeros((n,n))
        
        while self.calculateDeterminant(matrix) == 0:
            matrix = np.random.randint(1, 10, (n, n))
            
        return matrix
    
    
    def calculateDeterminant(self, matrix):
        """Výpočet determinantu matice
        
        Args:
            matrix (numpy array int):  matice, ve tvaru numpy array intů
            
        Returns:
            float: Hodnota determinantu matice
        """
        if matrix.shape[0] != matrix.shape[1]:
            return 0
        
        return np.linalg.det(matrix)
    
    
    def calculateInverseMatrix(self, matrix):
        """Výpočet inverzní matice

        Args:
            matrix (numpy array int): matice

        Returns:
            numpy array int: inverzní matice
        """
        if matrix.shape[0] != matrix.shape[1]:
            return 0
    
        return np.linalg.inv(matrix)
    
    
    def calculateRank(self, matrix):
        """Výpočet řádu matice

        Args:
            matrix (numpy array int): matice

        Returns:
            int: řád matice
        """
        return np.linalg.matrix_rank(matrix)
    
    
    def calculateEigenvalues(self, matrix):
        """Výpočet vlastních čísel matice

        Args:
            matrix (numpy array int): matice

        Returns:
            float: součet vlastní čísla matice
        """
        if matrix.shape[0] != matrix.shape[1]:
            return 0
        
        return sum(np.linalg.eigvals(matrix))
    
    
    def getLatexMatrix(self, matrix):
        """Metoda pro vygenerování matice ve formátu LaTeX

        Args:
            matrix (numpy.ndarray): matice

        Returns:
            string: matice ve formátu LaTeX
        """
        vypis = "\\\\begin{pmatrix}"
        
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                vypis+= matrix[i][j].__str__() 
                
                if j != matrix.shape[1]-1:
                    vypis+="&"
                    
            vypis+="\\\\\\\\" 
            
        return vypis+"\\\\end{pmatrix}"
    

    
    def generateQuestion(self, n = None):
        """Metoda na generování otázek na matice

        Returns:
            MatrixQuestionGenerator: Vrací sebe sama s vygenerovanými otázkami
        """
        if n is not None and n in range(0, 4):
            randomQuestion = n
            
        else:
            randomQuestion = random.randint(0, 3)
            
        matice = self.generateRegularMatrix()
        
        if randomQuestion == 0:
            matice = self.generateRegularMatrix(2)
            self.questionText ="Vypočti determinant matice: " 
            self.questionLatex = self.getLatexMatrix(matice)
            self.answer =self.calculateDeterminant(matice)
            
        elif randomQuestion == 1:
            self.questionText ="Vypočti determinant inverzní matice: " 
            self.questionLatex = self.getLatexMatrix(matice)
            self.answer =self.calculateDeterminant(self.calculateInverseMatrix(matice))
            
        elif randomQuestion == 2:
            self.questionText ="Vypočti hodnost matice: " 
            self.questionLatex = self.getLatexMatrix(matice)
            self.answer =self.calculateRank(matice)
            
        else:
            matice = self.generateRegularMatrix(2)
            self.questionText ="Vypočti součet vlastních čísel matice: " 
            self.questionLatex = self.getLatexMatrix(matice)
            self.answer = self.calculateEigenvalues(matice)
            
        return self
            
    
if __name__ == "__main__":
    mqg = MatrixQuestionGenerator()
    print (mqg.generateQuestion().__str__())