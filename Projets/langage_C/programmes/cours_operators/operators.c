#include <stdio.h>

int main(){
    int a;
    int b;
    int c;
    int d;
    int e = 8;
    float g = 9;
    char w = 'a';
    a = 2+3;
    b = a + 5;
    c = b / a;
    d = b % a;
    e*= 4;
    e--; // enleve 1
    e++; // ajoute 1
    g /= 2;
    w++;
    printf("Bienvenue\n");
    printf("a = %d\n",a);
    printf("b = %d\n",b);
    printf("c = %d\n",c);
    printf("d = %d\n",d);
    printf("e = %d\n",e);
    printf("g = %f\n",g);
    printf("w = %c\n",w);
    return 0;
}