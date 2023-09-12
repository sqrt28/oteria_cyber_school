#include <stdio.h>

int main()
{
    int variable = 15;
    int *pointeur = &variable;
    printf("pointeur = %p\n",pointeur);
    printf("%d\n",*pointeur);
    return 0;
}