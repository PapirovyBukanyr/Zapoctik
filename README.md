# Malý zápočtový projekt

Snad ten zápočet dostaneme

## Celkový popis

Hráč po spuštění aplikace bude mít možnost vybrat si z široké nabídky her (Šachy) a zahrát si je. Aby to nebylo tak snadné, tak před každým kolem se mu zobrazí matematická otázka, na kterou bude muset vymyslet odpověď.

## Autoři
 
 - Filip Brada
 - Vojtěch Hora
 - Marek Přibyl

## Použití

1. **Ujistěte se, že máte verzi Pythonu alespoň 3.6 nebo novější**

2. **Instalace závislostí**:
    ```sh
    pip install sympy numpy
    ```

3. **Spuštění generátoru otázek**:
    ```sh
    python main.py
    ```

## Složky a Soubory

### Backend šachů

 - TODO, Filip doplní

### Generování otázek

Otázky se generují v modulech `questions`, kde je třída `questions/Question.py`, ze které všechny otázky dědí a která poskytuje základní představu o struktuře generátorů. Další důležitá třída je `questions/GenerateQuestion.py`, která slouží k obecnému vygenerování otázky. Otázky na konkrétní témata se pak generují v souborech:
- `questions/generators/MatrixQuestionGenerator.py`: Generátor otázek na maticové operace.
- `questions/generators/FractionQuestionGenerator.py`: Generátor otázek na zlomky a obecně dvojice čísel.
- `questions/generators/DerivativeQuestionGenerator.py`: Generátor otázek na vyčíslování derivací.
- `questions/generators/LinearEquationSystemQuestionGenerator.py`: Generátor otázek na soustavy lineárních rovnic.


