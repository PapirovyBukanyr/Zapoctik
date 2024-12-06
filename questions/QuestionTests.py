from .generators import *
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
        ("Set", SetQuestionGenerator),
        ("Regular language", RegularLanguageQuestionGenerator)
    ]
    """list: Seznam všech tříd generátorů otázek
    """
    
    
    @parameterized.expand(allClasses)
    def testNumberOfQuestions(self, name, generator_class):
        """Testuje, zda se generuje nenulový počet otázek

        Args:
            name (string): jméno generátoru
            generator_class (Question): třída generátoru
        """
        generator = generator_class()
        self.assertGreater(generator.numberOfQuestions, 0)
        
    
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
            self.assertNotEqual(generator.questionText, "")
            self.assertNotEqual(generator.questionLatex, "")
        
        
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
            self.assertNotEqual(generator.doupovcuvOperator(), "")
            

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
            
    @parameterized.expand(allClasses)
    def testTimeSet(self, name, generator_class):
        generator = generator_class()
        
        for i in range(0, generator.numberOfQuestions):
            generator.generateQuestion(i)
            self.assertIsNotNone(generator.time)
            self.assertGreater(generator.time, 0)
            
    @parameterized.expand(allClasses)
    def testHoderova(self, name, generator_class):
        generator = generator_class()
        
        for i in range(0, generator.numberOfQuestions):
            generator.generateQuestion(i)
            self.assertIsNotNone(generator.hoderovaDanger)
