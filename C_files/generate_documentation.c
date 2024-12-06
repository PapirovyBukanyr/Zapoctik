#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <limits.h>


#define MAX_LINE_LENGTH 1024
#define LATEX_FILE "Dokumentace.tex"
#define PDF_FILE "Dokumentace.pdf"

int is_python_file(const char *filename) {
    const char *ext = strrchr(filename, '.');
    return ext && strcmp(ext, ".py") == 0;
}

void run_command(const char *command) {
    int result = system(command);
    if (result != 0) {
        fprintf(stderr, "Command failed: %s\n", command);
        exit(1);
    }
}

void process_python_file(const char *filepath, FILE *output) {
    char command[MAX_LINE_LENGTH];
    char temp_file[] = "temp_parsed.txt";

    snprintf(command, sizeof(command), "python C_files/parse_python.py \"%s\" > %s", filepath, temp_file);
    run_command(command);

    FILE *temp = fopen(temp_file, "r");
    if (!temp) {
        perror("Error opening temporary file");
        exit(1);
    }

    char line[MAX_LINE_LENGTH];
    while (fgets(line, sizeof(line), temp)) {
        for (char *p = line; *p; p++) {
            if (*p == '_' && *(p + 1) == '_') {
                *p = '\\';
            }
        }
        fprintf(output, "%s", line);
    }

    fclose(temp);
    remove(temp_file);
}

void process_directory(const char *dirpath, FILE *output) {
    DIR *dir = opendir(dirpath);
    if (!dir) {
        perror("Error opening directory");
        return;
    }

    struct dirent *entry;
    while ((entry = readdir(dir)) != NULL) {
        // Skip "." and ".."
        if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0) {
            continue;
        }

        char path[MAX_LINE_LENGTH];
        snprintf(path, sizeof(path), "%s/%s", dirpath, entry->d_name);

        struct stat path_stat;
        stat(path, &path_stat);

         if (S_ISDIR(path_stat.st_mode)) {
            process_directory(path, output); // Recursive call for subdirectories
        } else if (is_python_file(entry->d_name)) {
            printf("Processing file: %s\n", path);
            process_python_file(path, output);
        }
    }

    closedir(dir);
}

int main(int argc, char *argv[]) {
    FILE *output = fopen(LATEX_FILE, "w");
    if (!output) {
        perror("Error opening output file");
        return 1;
    }

    fprintf(output, "\\documentclass{article}\n");
    fprintf(output, "\\usepackage[utf8]{inputenc}\n");
    fprintf(output, "\\usepackage[czech]{babel}\n"); 
    fprintf(output, "\\usepackage{listings}\n");
    fprintf(output, "\\usepackage{color}\n");
    fprintf(output, "\\definecolor{keyword}{rgb}{0.0, 0.5, 0.0}\n");
    fprintf(output, "\\lstset{basicstyle=\\ttfamily,keywordstyle=\\color{keyword},commentstyle=\\itshape\\color{blue},escapeinside={\\%*}{*)}}\n"); // Ensure method names like __XY are not treated as subscript indices
    fprintf(output, "\\begin{document}\n");
    fprintf(output, "\\title{Dokumentace do projektu do matematického softwaru}\n");
    fprintf(output, "\\author{PříHoDa}\n");
    fprintf(output, "\\date{\\today}\n");
    fprintf(output, "\\maketitle\n");

    process_directory(".", output);

    fprintf(output, "\\end{document}\n");
    fclose(output);

    run_command("pdflatex " LATEX_FILE);

    return 0;
}
