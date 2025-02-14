#include<stdio.h>
//declaration prototype

void printhello();
void printgoodbye();
int main(){
 //function call
printhello();
printgoodbye();
return 0;
}


    
//function defination

void printhello(){
    printf("hello!\n");
}
void printgoodbye()  {
    printf("Goodbye\n");
}