#ifndef PYC_KILLER_H
#define PYC_KILLER_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <sys/stat.h>
#include <unistd.h>

// Funkce na mazani souboru s priponou .pyc
int process_directory(const char *dir_path);

#endif // PYC_KILLER_H