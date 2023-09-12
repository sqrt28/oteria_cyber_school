#include <stdio.h>

int main()
{   int nbr1;
    int nbr2 = 1;
    int res;
    printf("Combien font 2 * 2 ?");
    scanf("%d",&nbr1);
    while (nbr1  != 4)
    {
        printf("C'est Faux, réessayer\n");
        nbr2++;
        scanf("%d",&nbr1);
    }
    printf("BRAVO\n");
    printf("Vous avez réussi  avec %d essaies\n",nbr2);
    return 0;
}