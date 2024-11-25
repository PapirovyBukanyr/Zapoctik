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
    
    Pro hraní:
    ```sh
    pip install sympy numpy PyQt5 PyQtWebEngine
    ```

    Pro debugování a testování:
     ```sh
    pip install sympy numpy PyQt5 PyQtWebEngine parameterized unittest
    ```

3. **Spuštění aplikace**:
    ```sh
    python main.py
    ```

    Spuštění kontroly vracených hodnot hrami a otázkami
    ```sh
    python tests.py
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

#### Backend šachů s mlhou války

Jedná se prakticky o totožnou hru, jako je ta předchozí, jenom třída `games/ChessWithFogOfWar` modifikuje metodu getBoard tak, aby se zobrazovala pouze dostupná políčka.

#### Backend dámy

Většina logiky se nachází v modulu `games/checkers`. Hlavní třída, která vše řídí je `games/checkers/Checkers.py`, která zajišťuje výběr figurky, provedení tahu, střídání tahů a případné zjištění konce hry a její ukončení. Funkčnost desky zajišťuje třída `games/checkers/CheckersBoard.py`, která představuje šachovnici, primárně tedy slouží k ukládání pozic figur při hře. Dědí z `games/Board.py`. Dále je tam složka `games/checkers/pieces`, ve které se nachází všechny možné figurky. Všechny figury dědí z jedné mateřské třídy `games/checkers/pieces/Piece.py`, která předepisuje základní vlastnosti všech figur (např. pohyb po šachovnici). Konkrétní implementace jednotlivých figur jsou v souborech:
- `games/checkers/pieces/Queen.py`: Dáma
- `games/checkers/pieces/Pawn.py`: Pěšec

#### Backend dámy s mlhou války

Jedná se prakticky o totožnou hru, jako je ta předchozí, jenom třída `games/CheckersWithFogOfWar` modifikuje metodu getBoard tak, aby se zobrazovala pouze dostupná políčka.

#### Backend piškvorek 3x3

Většina backendu piškvorek se nachází v souboru `games/ticTacToe`, hlavní třída je `games/ticTacToe/TicTacToe.py`, ve které je většina logiky, dále tam je třída `games/ticTacToe/TicTacToeBoard.py`, která dědí z `games/Board.py`.

#### Backend matematické hry

Jde o hru, ve které se dva hráči pohybují podle zadání. mohou se pohybovat pouze nahoru a dolů, pohybují se dokud nenarazí na políčko s úkoly. Potom protější hráč začne hádat otázky. Pokud uhodne, získává bod a může hrát. Pokud ne, získává možnost odpovědět soupeř. Střídají se, dokud někdo neuhodne. Hra končí nalezením a zodpovězením desáté otázky. Vše se nacjází v modulu `games/mathGame`. Hlavní logika se nachází v souboru `games/mathGame/MathGame.py`. Dále je tam třída šachovnice `games/mathGame/MathGameBoard.py`, která dědí z `games/Board.py`.

#### Backend hry hledání krtka

Cílem hry je najít krtka, což je černý pěšák, na zakryté šachovnici. Ten za sebou zanechává stopu, tedy po odkrytí políčka se objeví číslo, před kolika tahy tam krtek byl. Maximum je historie osmi tahů. Zvláštností hry je, že se celý její kód nachází na jediném řádku ve třídě `games/ChallengeAccepted`. Tato hra vznikla jako protest proti nutné podmínce, že žádná funkce nesmí být delší než čtyřicet řádků. Snažíme se tím poukázat na to, že počet řádků není primární kritérium přehlednosti kódu.

#### Backend hry miny 

Veškerá logika hry je v `games/mines`. Hlavní třída je `games/mines/Mines`, kde je definována veškerá logika hry. Herní deska je definována ve třídě `games/mines/MinesBoard`, která stejně jako ostatní herní desky dědí z `games/Board`. Princip hry je lehce upraven pro dva hráče. To v praxi znamená, že za správně umístěnou vlaječku hráč získá bod, za odebrání správné vlaječky bod ztratí. Kdo má nakonec nejvíc bodů vítězí. 

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

### Testy

Abychom si usnadnili práci při debugování, byly stvořeny testy. Ty kontrolují pouze, zda se vrací správný datový typ. Primární logika je v `Tests.py`. Odtud se zavolají třídy pro kontrolu funkčnosti her `games/GameTests` a funkčnost generování otázek `questions/QuestionTests`. Jak již bylo řečeno, kontrolují ale pouze a jenom správnost vráceného návratového typu, ne jestli například odpověď na otázku dává smysl nebo jestli je otázka v češtině.

