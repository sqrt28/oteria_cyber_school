gcc test.c -o programme
./programme


Sur une variable, comme la variable age  :
age signifie : "Je veux la valeur de la variable age  " ;
&age signifie : "Je veux l'adresse à laquelle se trouve la variable age  ".

Sur un pointeur, comme pointeurSurAge  :
pointeurSurAge signifie : "Je veux la valeur de pointeurSurAge  " (cette valeur étant une adresse) ;
*pointeurSurAge signifie : "Je veux la valeur de la variable qui se trouve à l'adresse contenue dans pointeurSurAge  ".