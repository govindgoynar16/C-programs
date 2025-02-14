#include <stdio.h>
int main(){
int a,b,smallest;
printf("enter two number=");
scanf("%d %d",&a,&b);
smallest=(a<b)*a+(b<=a)*b;


printf("the smallest number is %d\n",smallest);

    return 0;
}