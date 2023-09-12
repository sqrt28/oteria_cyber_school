#include <stdio.h>

int main(){
    int a = 10;
    int b = 10;
    int c = 3;
    char mot1 = "salut";
    char mot2 = "hello";
    int res;
    int res1;
    int res2;
    res = (a == b); // (a != b) (a > b) etc .. renvoie 1 si vrai sinon 0
    res1 = (a==b) && (a > c); // and= && ou = ||
    res2 = mot1 == mot2;
    printf("res = %d\n",res);
    printf("res1 = %d\n",res1);
    printf("res2 = %d\n",res2);
    return 0;
}