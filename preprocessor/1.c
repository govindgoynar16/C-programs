#include<stdio.h>
#include<stdlib.h>
#define LIMIT 5
#define PI 3.14
#define PASSWORD "34ty56ui9o"
#define DISPLAY printf("hello govind")
int main(){
    int counter;
    for(counter=1;counter<=LIMIT;counter++)
    printf("%d\n",counter);

   printf("PI=%f\n",PI);
   printf("pass=%s\n",PASSWORD);
   DISPLAY;
    return 0;
}