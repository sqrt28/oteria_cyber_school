#include <stdio.h>

int main() {
    int a = 2;
    int b = 3;
    char c;
    if (a != 3) {
        printf("a différent de b\n");
    }
    if (a%2==0) {
        printf("a est pair\n");
    } else {
        printf("a est impair\n");
    }
    printf("c: %s\n",c);
    printf("a = %d\n",a);
    printf("b = %d\n",b);
    return 0;
}