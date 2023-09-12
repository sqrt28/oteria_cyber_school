#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define TAILLE_MAX 1000

int main(int argc, char *argv[])
{
    FILE* fichier = NULL;
    char chaine[TAILLE_MAX] = ""; // Chaîne vide de taille TAILLE_MAX
    int val;
 
    fichier = fopen("test_c.txt", "r+");
 
    if (fichier != NULL)
    {
        fgets(chaine, TAILLE_MAX, fichier); // On lit maximum TAILLE_MAX caractères du fichier, on stocke le tout dans "chaine"
        fputs(" sam",fichier);
        printf("%s", chaine); // On affiche la chaîne
        rename("test_c.txt","test_c_V2.txt");
        fclose(fichier);
    }

    scanf("%d",&val);

    if (val == 1)
    {
        remove("test_c_V2.txt");
    }
 
    return 0;
}
