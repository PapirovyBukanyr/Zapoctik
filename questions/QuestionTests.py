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
    @parameterized.expand([
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
    ])
    def testenerateQuestion(self, name, generator_class):
        generator = generator_class()
        question = generator.generateQuestion()
        self.assertIsNotNone(question)
        self.assertIsNotNone(generator.questionText)
        self.assertIsNotNone(generator.questionLatex)
        
        
    @parameterized.expand([
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
    ])
    def testDoupovcuvOperator(self, name, generator_class):
        generator = generator_class()
        question = generator.generateQuestion()
        self.assertIsNotNone(generator.doupovcuvOperator())


    @parameterized.expand([
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
    ])
    def testCheckAnswer(self, name, generator_class):
        generator = generator_class()
        question = generator.generateQuestion()
        self.assertTrue(generator.checkAnswer(generator.doupovcuvOperator()))
        

    @parameterized.expand([
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
    ])
    def testWrongAnswer(self, name, generator_class):
        generator = generator_class()
        question = generator.generateQuestion()
        self.assertFalse(generator.checkAnswer("Wrong answer"))
