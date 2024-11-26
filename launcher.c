#include <stdlib.h> 
#include <stdio.h>  
#include "C_files/pyc_killer.h"

/** 
 * Spusti skript pyc_killer.exe, ktery odstrani vsechny soubory s priponou .pyc v adresari a jeho podadresarich.
 * 
 * @return 0 pokud byl skript uspesne spusten
 * @return 1 pokud nastala chyba pri spousteni skriptu
 *
*/
int call_pyc_killer_3000() {

    printf("Spoustim skript pyc_killer 3000...\n");

    const char *start_dir = ".";
    if (process_directory(start_dir) != 0) {
        printf("Chyba pri spousteni skriptu pyc_killer 3000!\n");
        return 1;
    }
    
    printf("Genocida provedena s laskou.\n");

    return 0; 
}

/**
 * Instaluje potrebne Python knihovny a spusti skript main.py.
 * 
 * @return 0 pokud vse probehlo v poradku
 * @return 1 pokud nastala chyba pri instalaci knihoven
 * @return 2 pokud nastala chyba pri spousteni skriptu main.py
 * @return 3 pokud nastala chyba pri spousteni skriptu pyc_killer
 * @return 4 pokud nastala chyba pri kontrole verze Pythonu
 * @return 5 pokud nastala chyba pri stahovani nejnovejsi aktualizace z GitHubu
 */
int main() {
    char buffer[128];
    FILE *pipe = popen("python --version 2>&1", "r");
    if (!pipe) {
        printf("Chyba pri kontrole verze Pythonu!\n");
        return 4;
    }
    fgets(buffer, sizeof(buffer), pipe);
    pclose(pipe);

    int major, minor;
    if (sscanf(buffer, "Python %d.%d", &major, &minor) != 2) {
        printf("Chyba pri cteni verze Pythonu!\n");
        return 4;
    }

    if (major < 3 || (major == 3 && minor < 10)) {
        printf("Python verze 3.10 nebo vyssi je vyzadovana!\n");
        return 4;
    }
    else {
        printf("Program vyzaduje Python verze 3.10 nebo vyssi.\n");
        printf("Je nainstalovana verze Pythonu %d.%d.\n", major, minor);
    }

    printf("Kontrola nejnovejsi verze z GitHubu...\n");
    if (system("git pull") != 0) {
        printf("Chyba pri stahovani nejnovejsi verze z GitHubu!\n");
        return 5;
    }


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
