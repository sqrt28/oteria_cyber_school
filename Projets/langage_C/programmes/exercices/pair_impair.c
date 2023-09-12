#include <stdio.h>

int main()
{
    int nbre;
    printf("Saisissez un nombre : ");
    scanf("%d",&nbre);
    printf("%d\n",nbre);

    if (nbre % 2 == 0){
        printf("Le chiffre est pair\n");
    } 
    else{
        printf("Le chiffre est impair\n");
    }

}