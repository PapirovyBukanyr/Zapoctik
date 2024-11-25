from .generators import (
    MatrixQuestionGenerator,
    FractionQuestionGenerator,
    DerivativeQuestionGenerator,
    LinearEquationSystemQuestionGenerator,
    AnalyticGeometryQuestionGenerator,
    InfinitiveSeriesQuestionGenerator,
    IntegralQuestionGenerator,
    OrdinalNumberQuestionGenerator,
    KardinalNumberQuestionGenerator,
    SetQuestionGenerator
)
from .GenerateQuestion import GenerateQuestion
import unittest
from parameterized import parameterized

class QuestionTests(unittest.TestCase):
    """Testy na generátory otázek
    """
    
    
    allClasses = [
        ("General use", GenerateQuestion),
        ("Analytic geometry", AnalyticGeometryQuestionGenerator),
        ("Derivative", DerivativeQuestionGenerator),
        ("Fraction", FractionQuestionGenerator),
        ("Infinitive series", InfinitiveSeriesQuestionGenerator),
        ("Integral", IntegralQuestionGenerator),
        ("Kardinal numbers", KardinalNumberQuestionGenerator),
        ("Linear equation system", LinearEquationSystemQuestionGenerator),
        ("Matrix", MatrixQuestionGenerator),
        ("Ordinal numbers", OrdinalNumberQuestionGenerator),
        ("Set", SetQuestionGenerator)
    ]
    """list: Seznam všech tříd generátorů otázek
    """
        
    
    @parameterized.expand(allClasses)
    def testGenerateQuestion(self, name, generator_class):
        """Testuje, zda se vygeneruje otázka
        
        Args:
            name (string): jméno generátoru
            generator_class (Question): třída generátoru
        """
        generator = generator_class()
        
        for i in range(0, generator.numberOfQuestions):
            question = generator.generateQuestion(i)
            self.assertIsNotNone(question)
            self.assertIsNotNone(generator.questionText)
            self.assertIsNotNone(generator.questionLatex)
        
        
    @parameterized.expand(allClasses)
    def testDoupovcuvOperator(self, name, generator_class):
        """Testuje, zda se vygeneruje odpověď

        Args:
            name (string): jméno generátoru
            generator_class (Question): třída generátoru
        """
        generator = generator_class()
        
        for i in range(0,generator.numberOfQuestions):
            generator.generateQuestion(i)
            self.assertIsNotNone(generator.doupovcuvOperator())
            

    @parameterized.expand(allClasses)
    def testCheckAnswer(self, name, generator_class):
        """Testuje, zda je odpověď správná
        
        Args:
            name (string): jméno generátoru
            generator_class (Question): třída generátoru
        """
        generator = generator_class()
        
        for i in range(0, generator.numberOfQuestions):
            generator.generateQuestion(i)
            self.assertTrue(generator.checkAnswer(generator.doupovcuvOperator()))
            self.assertTrue(generator.checkAnswer(generator.doupovcuvOperator().upper()))
            self.assertTrue(generator.checkAnswer(generator.doupovcuvOperator().lower()))
        

    @parameterized.expand(allClasses)
    def testWrongAnswer(self, name, generator_class):
        """Testuje, zda je odpověď špatná
        
        Args:
            name (string): jméno generátoru
            generator_class (Question): třída generátoru
        """
        generator = generator_class()
        
        for i in range(0, generator.numberOfQuestions):
            generator.generateQuestion(i)
            self.assertFalse(generator.checkAnswer("Wrong answer"))
