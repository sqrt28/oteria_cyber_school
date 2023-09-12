#include <stdio.h>
#include <string.h>


int main()
{
    char chaine[] = "salut", copie[10];
    int longueur = strlen(chaine);
    char chaine1[100] = "bonjour";
    char chaine2[] = "sam";
    strcat(chaine1, chaine2);
    printf("La chaine %s est de longueur %d\n",chaine,longueur);
    printf("La copie de la chaine est %s\n",strcpy(copie,chaine));
    printf("%s\n",chaine1);
    if (strcmp(chaine1, chaine2) == 0) // Si chaînes identiques
    {
        printf("Les chaines sont identiques\n");
    }
    else
    {
        printf("Les chaines sont differentes\n");
    }
    return 0;
}