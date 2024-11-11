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
        
    
    @parameterized.expand(allClasses)
    def testGenerateQuestion(self, name, generator_class):
        generator = generator_class()
        question = generator.generateQuestion()
        self.assertIsNotNone(question)
        self.assertIsNotNone(generator.questionText)
        self.assertIsNotNone(generator.questionLatex)
        
        
    @parameterized.expand(allClasses)
    def testDoupovcuvOperator(self, name, generator_class):
        generator = generator_class()
        generator.generateQuestion()
        self.assertIsNotNone(generator.doupovcuvOperator())


    @parameterized.expand(allClasses)
    def testCheckAnswer(self, name, generator_class):
        generator = generator_class()
        generator.generateQuestion()
        self.assertTrue(generator.checkAnswer(generator.doupovcuvOperator()))
        

    @parameterized.expand(allClasses)
    def testWrongAnswer(self, name, generator_class):
        generator = generator_class()
        generator.generateQuestion()
        self.assertFalse(generator.checkAnswer("Wrong answer"))
