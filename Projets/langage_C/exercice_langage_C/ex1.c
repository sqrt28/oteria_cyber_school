#include <stdio.h>

int main()
{   int nbr1;
    int nbr2;
    int res;
    printf("Donner un chiffre ou nombre");
    scanf("%d",&nbr1);
    printf("Donner un chiffre ou nombre //ATTENTION division par 0 impossible");
    scanf("%d",&nbr2);
    while (nbr2 == 0){
        printf("//ATTENTION division par 0 impossible//");
        scanf("%d",&nbr2);
    }
    res = nbr1 / nbr2;

    printf("Le résultat de nbr1 / nbr2 est %d\n",res);
    return 0;
}