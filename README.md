# Malý zápočtový projekt

Snad ten zápočet dostaneme

## Celkový popis

Hráč po spuštění aplikace bude mít možnost vybrat si z široké nabídky her (Šachy) a zahrát si je. Aby to nebylo tak snadné, tak před každým kolem se mu zobrazí matematická otázka, na kterou bude muset vymyslet odpověď.

## Autoři
 
 - Filip Brada
 - Vojtěch Hora
 - Marek Přibyl

## Použití

1. **Ujistěte se, že máte verzi Pythonu alespoň 3.10 nebo novější**

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

Celá logika se nachází ve složce `chess`. Řízení chodu celé hry má na starosti třída `chess/GameController.py`, která zajišťuje výběr figurky, provedení tahu, střídání tahů a případné zjištění konce hry a její ukončení. Hlubší funkcionalitu jednak zajišťuje třída `chess/Board.py`, která představuje šachovnici, primárně tedy slouží k ukládání pozic figur při hře. A jednak složka `chess/pieces`, ve které se nachází právě funkcionalita všech šachových figur. Všechny figury dědí z jedné mateřské třídy `chess/pieces/Piece.py`, která předepisuje základní vlastnosti všech figur (např. pohyb po šachovnici). Konkrétní implementace jednotlivých figur, obsahující informace o možnosti tahů, symbolu dané figury v notaci nebo materiálové hodnoty figury, se pak nachází v souborech:
- `chess/pieces/King.py`: Král
- `chess/pieces/Queen.py`: Dáma
- `chess/pieces/Rook.py`: Věž
- `chess/pieces/Knight.py`: Jezdec
- `chess/pieces/Bishop.py`: Střelec
- `chess/pieces/Pawn.py`: Pěšec

### Generování otázek

Otázky se generují v modulech `questions`, kde je třída `questions/Question.py`, ze které všechny otázky dědí a která poskytuje základní představu o struktuře generátorů. Další důležitá třída je `questions/GenerateQuestion.py`, která slouží k obecnému vygenerování otázky. Otázky na konkrétní témata se pak generují v souborech:
- `questions/generators/MatrixQuestionGenerator.py`: Generátor otázek na maticové operace.
- `questions/generators/FractionQuestionGenerator.py`: Generátor otázek na zlomky a obecně dvojice čísel.
- `questions/generators/DerivativeQuestionGenerator.py`: Generátor otázek na vyčíslování derivací.
- `questions/generators/LinearEquationSystemQuestionGenerator.py`: Generátor otázek na soustavy lineárních rovnic.


