#include <stdlib.h> 
#include <stdio.h>  

int main() {
    printf("Instalace požadovaných Python knihoven...\n");
    
    if (system("pip install sympy numpy PyQt5 PyQtWebEngine") != 0) {
        printf("Chyba při instalaci knihoven!\n");
        return 1; 
    }

    printf("Knihovny úspěšně nainstalovány.\n");

    printf("Spouštím skript main.py...\n");
    if (system("python main.py") != 0) {
        printf("Chyba při spouštění skriptu main.py!\n");
        return 1;
    }

    printf("Skript main.py byl úspěšně spuštěn.\n");


    printf("Mazání stop za pomocí luxusního pyc killeru 3000...\n");
    if (system("pyc_killer.exe") != 0) {
        printf("Chyba při spouštění skriptu pyc_killer.exe!\n");
        return 1; 
    }

    printf("Genocida provedena.\n");

    return 0; 
}
