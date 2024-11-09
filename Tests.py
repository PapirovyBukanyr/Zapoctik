import unittest
from questions.QuestionTests import QuestionTests
from games.GameTests import GameTests

numberOfTests = 100
success = 0

loader = unittest.TestLoader()

for i in range(numberOfTests):
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(QuestionTests))
    suite.addTests(loader.loadTestsFromTestCase(GameTests))
    
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    if result.wasSuccessful():
        success += 1
    else:
        print("Test failed")
        break

print("Úspěšnost testů: ", success / numberOfTests)