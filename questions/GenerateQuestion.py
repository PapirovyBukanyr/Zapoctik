import random as rand

class GenerateQuestion:
    """_summary_ Třída na generování otázek
    Pro generování otázek použij metodu generateQuestion
    """
    def __init__(self):
        self.loadQuestions()
        print("Otázky jsou připraveny ke generování")
        
    def loadQuestions(self):
        """_summary_ Metoda na načtení otázek
        """
        self.questions = ["Kolik je 2+2?", "Kolik je 3*3?", "Kolik je 4-2?", "Kolik je 5/5?"]
        self.answers = [4,9,2,1]
        
    def generateQuestion(self):
        """_summary_ Metoda na generování otázek
        Metoda náhodně vybere náhodnou otázku ze seznamu a vrátí ji
        _return_ otázka ve formátu string
        """
        self.numberOfChosenQustion = rand.randint(0, self.questions.count()-1) 
        return self.questions[self.numberOfChosenQustion]
    
    def checkAnswer(self, answer):
        """_summary_ Metoda na kontrolu odpovědi
        Metoda zkontroluje zda je zadaná odpověď správná
        _param_ answer - zadaná odpověď
        _return_ True - pokud je odpověď správná
        """
        if answer == self.answers[self.numberOfChosenQustion]:
            return True
        else:
            return False
    