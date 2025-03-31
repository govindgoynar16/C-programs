 #include<stdio.h>
#include<stdlib.h>
#define ONE 1
#define AND &&
#define OR ||
#define TWO ONE+ONE
#define THREE TWO+ONE
#define MESSAGE "this is\
 a very long\
  message"
  #define SQUARE(x) x*x
int main(){

    // if(1 AND 1)
    // printf("something true\n");
    // printf("%d\n",THREE);
    // printf("%s",MESSAGE); 
    int result =SQUARE(10);
    printf("result=%d\n",result);
    return 0;
}