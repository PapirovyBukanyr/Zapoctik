#include "pyc_killer.h"

/**
 * Smaze soubor na zadanem miste.
 * 
 * @param path Cesta k souboru
 * 
 * @return void
 */
void delete_file(const char *path) {
    if (unlink(path) == 0) {
        printf("Deleted: %s\n", path);
    } else {
        perror("Error deleting file");
    }
}


/**
 * Rekurzivne projde adresar a jeho podadresare a smaze vsechny soubory s priponou .pyc.
 * 
 * @param dir_path Cesta k adresari
 * 
 * @return int 0 pokud vse probehlo v poradku
 * @return int 1 pokud nastala chyba pri otevirani adresare
 */
int process_directory(const char *dir_path) {
    DIR *dir = opendir(dir_path);

    if (dir == NULL) {
        perror("Error opening directory");
        return 1;
    }

    struct dirent *entry;
    char full_path[4096];

    while ((entry = readdir(dir)) != NULL) {
        if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0) {
            continue;
        }

        snprintf(full_path, sizeof(full_path), "%s/%s", dir_path, entry->d_name);

        struct stat path_stat;

        if (stat(full_path, &path_stat) != 0) {
            perror("Error reading file stats");
            continue;
        }

        if (S_ISDIR(path_stat.st_mode)) {
            if (process_directory(full_path) != 0) {
                return 1;
            }
        } 
        else if (S_ISREG(path_stat.st_mode)) {
            const char *ext = strrchr(entry->d_name, '.');

            if (ext != NULL && strcmp(ext, ".pyc") == 0) {
                delete_file(full_path);
            }
        }
    }

    closedir(dir);
    
    return 0;
}