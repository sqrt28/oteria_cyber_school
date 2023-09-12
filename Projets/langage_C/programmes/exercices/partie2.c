#include <stdio.h>

int main()
{   
    int reponse;
    printf("1 : royal cheese, 2 : deluxe, 3 : big mac\n");
    scanf("%d",&reponse);
    switch (reponse)
    {
    case 1:
        printf("votre choix est royal cheese\n");
        break;
    case 2:
        printf("votre choix est le deluxe\n");
        break;
    case 3:
        printf("votre choix est le big mac\n");
        break;

    default:
        printf("ce numéro ne correspond à aucun burger\n");
        break;
    }
    return 0;
}