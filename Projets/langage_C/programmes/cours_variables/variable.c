#include <stdio.h>

int main( ){
    int nombre_entier; //déclaration de variable
    float nombre_decimal = 49.3;
    char caractere = 'o';
    nombre_entier = 42; //affectation de 42 à nombre_entier

    printf("Bienvenue dans notre programme\n");
    printf("un entier --> %d\n",nombre_entier);
    printf("un float --> %f\n",nombre_decimal);
    printf("un caractere --> %c\n",caractere);
    printf("un caractere %c à la valeur %d\n",caractere,caractere);
    return 0;
}