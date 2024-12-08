#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>

#define MAX_LINE_LENGTH 1024
#define LATEX_FILE "Dokumentace.tex"

// Funkce kontrolující, zda je název složky nebo souboru na seznamu ignorovaných
int is_ignored(const char *name) {
    const char *ignored[] = {".git", NULL}; // Seznam ignorovaných složek nebo souborů
    for (int i = 0; ignored[i] != NULL; i++) {
        if (strcmp(name, ignored[i]) == 0) {
            return 1; // Název je na seznamu ignorovaných
        }
    }
    return 0; // Název není ignorován
}

int is_python_file(const char *filename) {
    const char *ext = strrchr(filename, '.');
    return ext && strcmp(ext, ".py") == 0;
}

void run_command(const char *command) {
    int result = system(command);
    if (result != 0) {
        fprintf(stderr, "Příkaz selhal: %s\n", command);
        exit(1);
    }
}

void sanitize_latex(char *text) {
    char *p = text;
    while (*p) {
        if (*p == '_') {
            memmove(p + 1, p, strlen(p) + 1); // Posuň text
            *p = '\\';
            p += 2;
        } else {
            p++;
        }
    }
}

void process_python_file(const char *filepath, FILE *output) {
    char command[MAX_LINE_LENGTH];
    char temp_file[] = "temp_parsed.txt";

    snprintf(command, sizeof(command), "python3 C_files/parse_python.py \"%s\" \"%s\"", filepath, temp_file);
    run_command(command);

    FILE *temp = fopen(temp_file, "r");
    if (!temp) {
        perror("Chyba při otevírání dočasného souboru");
        exit(1);
    }

    char line[MAX_LINE_LENGTH];
    while (fgets(line, sizeof(line), temp)) {
        sanitize_latex(line);
        fprintf(output, "%s", line);
    }

    fclose(temp);
    remove(temp_file);
}

void process_directory(const char *dirpath, FILE *output, int depth) {
    DIR *dir = opendir(dirpath);
    if (!dir) {
        perror("Chyba při otevírání složky");
        return;
    }

    struct dirent *entry;
    while ((entry = readdir(dir)) != NULL) {
        if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0 || is_ignored(entry->d_name)) {
            continue;
        }

        char path[MAX_LINE_LENGTH];
        snprintf(path, sizeof(path), "%s/%s", dirpath, entry->d_name);

        struct stat path_stat;
        stat(path, &path_stat);

        if (S_ISDIR(path_stat.st_mode)) {
            sanitize_latex(entry->d_name);
            fprintf(output, "\\section*{Složka: %s}\n", entry->d_name);
            process_directory(path, output, depth + 1);
        } else if (is_python_file(entry->d_name)) {
            fprintf(output, "\\subsection*{Soubor: %s}\n", entry->d_name);
            process_python_file(path, output);
        }
    }

    closedir(dir);
}

int main(int argc, char *argv[]) {
    FILE *output = fopen(LATEX_FILE, "w");
    if (!output) {
        perror("Chyba při otevírání výstupního souboru");
        return 1;
    }

    fprintf(output, "\\documentclass{article}\n");
    fprintf(output, "\\usepackage[utf8]{inputenc}\n");
    fprintf(output, "\\usepackage[czech]{babel}\n");
    fprintf(output, "\\usepackage{listings}\n");
    fprintf(output, "\\usepackage{color}\n");
    fprintf(output, "\\definecolor{keyword}{rgb}{0.0, 0.5, 0.0}\n");
    fprintf(output, "\\lstset{basicstyle=\\ttfamily,keywordstyle=\\color{keyword},commentstyle=\\itshape\\color{blue},escapeinside={\\%*}{*)}}\n");
    fprintf(output, "\\begin{document}\n");
    fprintf(output, "\\title{Dokumentace projektu}\n");
    fprintf(output, "\\author{PříHoDa}\n");
    fprintf(output, "\\date{\\today}\n");
    fprintf(output, "\\maketitle\n");

    process_directory(".", output, 0);

    fprintf(output, "\\end{document}\n");
    fclose(output);

    run_command("pdflatex " LATEX_FILE);

    return 0;
}
