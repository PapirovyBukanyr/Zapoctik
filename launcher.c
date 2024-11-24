#include <stdlib.h> 
#include <stdio.h>  

int call_pyc_killer_3000() {

    printf("Spoustim skript pyc_killer.exe...\n");

    if (system("pyc_killer.exe") != 0) {
        printf("Chyba pri spousteni skriptu pyc_killer.exe!\n");
        return 1; 
    }
    
    printf("Genocida provedena.\n");

    return 0; 
}

int main() {
    printf("Instalace pozadovanych Python knihoven...\n");
    
    if (system("pip install sympy numpy PyQt5 PyQtWebEngine") != 0) {
        printf("Chyba pri instalaci knihoven!\n");
        return 1; 
    }

    printf("Knihovny uspesne nainstalovany.\n");

    printf("Spoustim skript main.py...\n");
    if (system("python main.py") != 0) {
        printf("Chyba pri spousteni skriptu main.py!\n");
        call_pyc_killer_3000();
        return 2;
    }

    printf("Skript main.py byl uspesne spusten.\n");

    if (call_pyc_killer_3000() != 0) {
        return 3; 
    }

    return 0; 
}
