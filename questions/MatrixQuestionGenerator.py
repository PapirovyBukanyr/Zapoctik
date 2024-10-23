import numpy as np
import sympy as sp
import random
from Question import Question

class MatrixQuestionGenerator(Question):  
    """Generátor otázek na matice
    """  
    def generateRegularMatrix(self):
        """Generování regulární matice

        Returns:
            Náhodná regulární matice, ve tvaru numpy array intů
        """
        n = random.randint(2, 4)
        matrix = np.zeros((n,n))
        while self.calculateDeterminant(matrix) == 0:
            matrix = np.random.randint(1, 10, (n, n))
        return matrix
    
    def calculateDeterminant(self, matrix):
        """Výpočet determinantu matice
        
        Args:
            matrix: matice, ve tvaru numpy array intů
            
        Returns:
            Hodnota determinantu matice
        """
        if matrix.shape[0] != matrix.shape[1]:
            return 0
        return np.linalg.det(matrix)
    
    def calculateInverseMatrix(self, matrix):
        """Výpočet inverzní matice

        Args:
            matrix: matice, ve tvaru numpy array intů

        Returns:
            matice, ve tvaru numpy array intů
        """
        if matrix.shape[0] != matrix.shape[1]:
            return 0
        return np.linalg.inv(matrix)
    
    def calculateRank(self, matrix):
        """Výpočet řádu matice

        Args:
            matrix: matice ve tvaru numpy array intů

        Returns:
            int: řád matice
        """
        return np.linalg.matrix_rank(matrix)
    
    def calculateEigenvalues(self, matrix):
        """Výpočet vlastních čísel matice

        Args:
            matrix: matice, ve tvaru numpy array intů

        Returns:
            numpy list: vlastní čísla matice
        """
        if matrix.shape[0] != matrix.shape[1]:
            return 0
        return np.linalg.eig(matrix)
    
    def vypis(self, matrix):
        """Metoda pro vygenerování matice ve formátu LaTeX

        Args:
            matrix: matice, ve tvaru numpy array intů

        Returns:
            string: matice ve formátu LaTeX
        """
        vypis = "$$\\begin{pmatrix}\n"
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                vypis+= matrix[i][j].__str__() 
                if j != matrix.shape[1]-1:
                    vypis+="&"
            vypis+="\\\\\n"
        vypis+="\\end{pmatrix}$$"
        return vypis
    
    def generateQuestion(self):
        """Metoda na generování otázek na matice

        Returns:
            Vrací sebe sama
        """
        randomQuestion = np.random.randint(1, 4)
        matice = self.generateRegularMatrix()
        if randomQuestion == 1:
            self.question ="Vypočti determinant matice: " + self.vypis(matice)
            self.answer =self.calculateDeterminant(matice)
        elif randomQuestion == 2:
            self.question ="Vypočti determinant inverzní matice: " + self.vypis(matice)
            self.answer =self.calculateDeterminant(self.calculateInverseMatrix(matice))
        elif randomQuestion == 3:
            self.question ="Vypočti hodnost matice: " + self.vypis(matice)
            self.answer =self.calculateRank(matice)
        else:
            self.question ="Vypočti součet vlastních čísel matice: " + self.vypis(matice)
            self.answer = sum(self.calculateEigenvalues(matice))
        return self
            
    
if __name__ == "__main__":
    mqg = MatrixQuestionGenerator()
    print (mqg.generateQuestion().__str__())
    