#include <stdio.h>
#include <string.h>


typedef struct Personne Personne;
struct Personne
{
    char nom[10];
    char prenom[10];
};

int main(int argc, char *argv[])
{
    Personne utilisateur;

    printf("Quel est votre nom ? ");
    scanf("%s", &utilisateur.nom);
    printf("Votre prenom ? ");
    scanf("%s", &utilisateur.prenom);

    printf("Vous vous appelez %s %s", utilisateur.prenom, utilisateur.nom);

    return 0;
}