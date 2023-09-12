#include <stdio.h>

void est_pair(int nombre)
{   
    if (nombre % 2 == 0)
    {
        printf("votre nomhre est pair\n");
    }
    else
    {
        printf("votre nomhre est impair\n");
    }
}

int main()
{   
    int nbr_usr;
    printf("saississez un nombre :\t");
    scanf("%d",&nbr_usr);
    est_pair(nbr_usr);
    return 0;
}
