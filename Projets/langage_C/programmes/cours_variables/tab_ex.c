#include <stdio.h>

int sommeTableau(int tableau[], int tailleTableau);
double moyenneTableau(int tableau[], int tailleTableau);

int main()
{
    int tab[] = {10,2,28,7};
    printf("la somme du tableau est de %d\n",sommeTableau(tab,4));
    printf("la moyenne du tableau est de %f\n",moyenneTableau(tab,4));
    return 0;
}

int sommeTableau(int tableau[],int tailleTableau)
{   
    int i,somme;
    for (i = 0; i < tailleTableau; i++)
    {
        somme += tableau[i];
    }
    return somme;
}

double moyenneTableau(int tableau[], int tailleTableau)
{
    int i,somme;
    double moyenne;
    for (i = 0; i < tailleTableau; i++)
    {
        somme += tableau[i];
    }
    moyenne = somme / tailleTableau;
    return moyenne;
}