from questions.GenerateQuestion import GenerateQuestion

# Zde se to pak celé spustí


# ukázka použití generátoru otázek, odpovědi se zaokrouhlují na celá čísla
qg = GenerateQuestion()
qg.generateQuestion() # automaticky vypíše otázku i s odpovědí do terminálu, nechal bych to kvůli debugování, klidně to odstraním. Marek
print("Odpověď: "+qg.doupovcuvOperator()) 
if qg.checkAnswer(input("Zadej odpověď: ")):
    print("Správně")
else:
    print("Špatně")