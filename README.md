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

### Backend her

Všechny hry se nachází v modulu `games`. Každá hra používá jednotnou brací desku `games/Board.py`. Společný je také soubor `games/Enums.py`, který obsahuje třídy typu enum "Figure" (co za figurku má frontend vykreslit), Colors (Barvy jsou "WHITE" a "BLACK") a "Field" (datová struktura kombinující předchozí dvě, určená ke komunikaci s Frontendem)

#### Backend šachů

Celá logika se nachází ve složce `games/chess`. Řízení chodu celé hry má na starosti třída `games/chess/Chess.py`, která zajišťuje výběr figurky, provedení tahu, střídání tahů a případné zjištění konce hry a její ukončení. Hlubší funkcionalitu jednak zajišťuje třída `games/chess/ChessBoard.py`, která představuje šachovnici, primárně tedy slouží k ukládání pozic figur při hře. A jednak složka `games/chess/pieces`, ve které se nachází právě funkcionalita všech šachových figur. Všechny figury dědí z jedné mateřské třídy `games/chess/pieces/Piece.py`, která předepisuje základní vlastnosti všech figur (např. pohyb po šachovnici). Konkrétní implementace jednotlivých figur, obsahující informace o možnosti tahů, symbolu dané figury v notaci nebo materiálové hodnoty figury, se pak nachází v souborech:
- `games/chess/pieces/King.py`: Král
- `games/chess/pieces/Queen.py`: Dáma
- `games/chess/pieces/Rook.py`: Věž
- `games/chess/pieces/Knight.py`: Jezdec
- `games/chess/pieces/Bishop.py`: Střelec
- `games/chess/pieces/Pawn.py`: Pěšec

#### Backend dámy

Většina logiky se nachází v modulu `games/checkers`. Hlavní třída, která vše řídí je `games/checkers/Checkers.py`, která zajišťuje výběr figurky, provedení tahu, střídání tahů a případné zjištění konce hry a její ukončení. Funkčnost desky zajišťuje třída `games/checkers/CheckersBoard.py`, která představuje šachovnici, primárně tedy slouží k ukládání pozic figur při hře. Dědí z `games/Board.py`. Dále je tam složka `games/checkers/pieces`, ve které se nachází všechny možné figurky. Všechny figury dědí z jedné mateřské třídy `games/checkers/pieces/Piece.py`, která předepisuje základní vlastnosti všech figur (např. pohyb po šachovnici). Konkrétní implementace jednotlivých figur jsou v souborech:
- `games/checkers/pieces/Queen.py`: Dáma
- `games/checkers/pieces/Pawn.py`: Pěšec

#### Backend piškvorek 3x3

Většina backendu piškvorek se nachází v souboru `games/ticTacToe`, hlavní třída je `games/ticTacToe/TicTacToe.py`, ve které je většina logiky, dále tam je třída `games/ticTacToe/TicTacToeBoard.py`, která dědí z `games/Board.py`.

### Backend generování otázek

Otázky se generují v modulech `questions`, kde je třída `questions/Question.py`, ze které všechny otázky dědí a která poskytuje základní představu o struktuře generátorů. Další důležitá třída je `questions/GenerateQuestion.py`, která slouží k obecnému vygenerování otázky. Otázky na konkrétní témata se pak generují v souborech:
- `questions/generators/MatrixQuestionGenerator.py`: Generátor otázek na maticové operace.
- `questions/generators/FractionQuestionGenerator.py`: Generátor otázek na zlomky a obecně dvojice čísel.
- `questions/generators/DerivativeQuestionGenerator.py`: Generátor otázek na vyčíslování derivací.
- `questions/generators/LinearEquationSystemQuestionGenerator.py`: Generátor otázek na soustavy lineárních rovnic.
- `questions/generators/AnalyticGeometryQuestionGenerator.py`: Generátor otázek na analytickou geometrii.
- `questions/generators/InfinitiveSeriesQuestionGenerator.py`: Generátor otázek na nekonečné řady.
- `questions/generators/IntegralQuestionGenerator.py`: Generátor otázek na integrály.
- `questions/generators/OrdinalNumberQuestionGenerator.py`: Generátor otázek na ordinální čísla.
- `questions/generators/KardinalNumberQuestionGenerator.py`: Generátor otázek na kardinální čísla.
- `questions/generators/SetQuestionGenerator.py`: Generátor otázek na množiny.

