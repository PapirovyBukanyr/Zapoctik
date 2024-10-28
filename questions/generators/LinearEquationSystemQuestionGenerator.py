import random
import sympy as sp
from questions.Question import Question

class LinearEquationSystemQuestionGenerator(Question):
    
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
            lhs = sum(random.randint(-10, 10) * var for var in variables)
            rhs = random.randint(-10, 10)
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
        result = "\\begin{align*}"
        for eq in equations:
            lhs = eq.lhs
            rhs = eq.rhs
            result += f"{sp.latex(lhs)} &= {sp.latex(rhs)}\\\\ "
        return result + "\\end{align*}"
    
    def generateQuestion(self):
        """Metoda na generování otázky

        Returns:
            LinearEquationSystemQuestionGenerator: Funkce vrací sebe sama s vygenerovanou otázkou
        """
        num_equations = random.randint(2, 4)
        num_variables = num_equations 
        equations, variables = self.generateLinearEquationSystem(num_equations, num_variables)
        
        # Za tuto rekurzi už se pro mě v pekle chystá kotel, ale nic lepšího mě teď nenapadá
        try:
            solution = sp.linsolve(equations, variables)
            self.answer = sum(next(iter(solution))).__str__()
            self.questionText = "Vyřeš soustavu rovnic, jako výsledek zapiš součet, pro zlomky ve tvaru a/b: "
            self.questionLatex = self.convert_to_latex(equations)
        except:
            self.generateQuestion()
            
        return self

if __name__ == "__main__":
    lesqg = LinearEquationSystemQuestionGenerator()
    print(lesqg.generateQuestion().__str__())