#include <stdio.h>

int main()
{
    int tab[3];
    int i;
    tab[0] = 2;
    tab[1] = 3;
    tab[2] = 2;

    for (;i<3;i++)
    {
        printf("tab[i] = %d\n",tab[i]);
    }

    printf("mon premier ele du tab vaut %d\n",tab[0]);
}