#include <stdio.h>

int main()
{   int nbr1;
    int nbr2 = 1;
    printf("Enter a number");
    scanf("%d",&nbr1);
    for (nbr2 =0; nbr2 < nbr1;nbr2++)
    {
        if (nbr2 % 2 == 0){
            printf("%d\n",nbr2);
        }

    }
    return 0;
}