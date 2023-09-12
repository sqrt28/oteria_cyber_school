#include <stdio.h>

int main()
{   int nbr1;
    int nbr2;
    int res;
    printf("////Ce programme permet de vérifier si le chiffre/nombre est pair ou impair///// \n");
    printf("Entrer un chiffre/nombre\n");
    scanf("%d",&nbr1);
    if (nbr1 % 2 == 0)
    {
        printf("C'est pair\n");
    }
    else
    {
        printf("ce n'est pas pair\n");
    }
    return 0;
}