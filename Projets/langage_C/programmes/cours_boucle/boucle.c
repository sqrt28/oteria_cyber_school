#include <stdio.h>

int main()
{
    int i = 0;
    int j = 0;
    int e;

    while (i < 10)
    {
        printf("i = %d\n",i);
        i++;
    }
    
    do 
    {
     printf("j = %d\n",j);
     j++;   
    } while (j < 10);

    for (e = 0; e < 10; e++)
    {
        printf("e = %d\n",e);
    }
}