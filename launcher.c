#include <stdlib.h> 
#include <stdio.h>  
/** 
 * Spusti skript pyc_killer.exe, ktery odstrani vsechny soubory s priponou .pyc v adresari a jeho podadresarich.
 * 
 * @return 0 pokud byl skript uspesne spusten
 * @return 1 pokud nastala chyba pri spousteni skriptu
 *
*/
int call_pyc_killer_3000() {

    printf("Spoustim skript pyc_killer.exe...\n");

    if (system("pyc_killer.exe") != 0) {
        printf("Chyba pri spousteni skriptu pyc_killer.exe!\n");
        return 1; 
    }
    
    printf("Genocida provedena.\n");

    return 0; 
}

/**
 * Instaluje potrebne Python knihovny a spusti skript main.py.
 * 
 * @return 0 pokud vse probehlo v poradku
 * @return 1 pokud nastala chyba pri instalaci knihoven
 * @return 2 pokud nastala chyba pri spousteni skriptu main.py
 * @return 3 pokud nastala chyba pri spousteni skriptu pyc_killer.exe
 */
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
