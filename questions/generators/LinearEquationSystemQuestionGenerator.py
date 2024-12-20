import random
import sympy as sp
from ..Question import Question

class LinearEquationSystemQuestionGenerator(Question):
    """Generátor otázek na lineární soustavy rovnic
    """
    
    
    def __init__(self):
        """Konstruktor třídy soustav lineárních rovnic
        """
        super().__init__()
        self.time = 120
        self.numberOfQuestions = 1
    
    
    def generateLinearEquationSystem(self, num_equations, num_variables):
        """Vygenerování lineární soustavy rovnic

        Args:
            num_equations (int): počet chtěných rovnic
            num_variables (int): počet chtěných proměnných

        Returns:
            sympy equations, sympy symbols: Vygenerované rovnice a jejich proměnné
        """
        variables = sp.symbols(f'x1:{num_variables+1}')
        equations = []
    
        for _ in range(num_equations):
            lhs = sum(random.randint(-5, 5) * var for var in variables)
            rhs = random.randint(-5, 5)
            equation = sp.Eq(lhs, rhs)
            equations.append(equation)
    
        return equations, variables
    
    
    def convert_to_latex(self, equations):
        """Metoda na konverzi rovnic do latexu

        Args:
            equations (sympy equations): vstupní rovnice

        Returns:
            string: latexový zápis rovnic ve formátu string
        """
        result = ""
        
        for eq in equations:
            lhs = eq.lhs
            rhs = eq.rhs
            result += f"{sp.latex(lhs)} = {sp.latex(rhs)}\\\\newline "
            
        return result + ""
    
    
    def generateQuestion(self, n = None):
        """Metoda na generování otázky
        
        Args:
            n (int): Číslo otázky, defaultně náhodné

        Returns:
            LinearEquationSystemQuestionGenerator: Funkce vrací sebe sama s vygenerovanou otázkou
        """
        num_equations = random.randint(2, 3)
        num_variables = num_equations 
        equations, variables = self.generateLinearEquationSystem(num_equations, num_variables)
        
        # Za tuto rekurzi už se pro mě v pekle chystá kotel, ale nic lepšího mě teď nenapadá
        try:
            solution = sp.linsolve(equations, variables)
            self.answer = sum(next(iter(solution))).__str__()
            self.questionText = "Vyřeš soustavu rovnic, jako výsledek zapiš součet, pro zlomky ve tvaru a/b: "
            self.questionLatex = self.convert_to_latex(equations)
    
        except:
            return self.generateQuestion()
            
        return self


if __name__ == "__main__":
    lesqg = LinearEquationSystemQuestionGenerator()
    print(lesqg.generateQuestion().__str__())