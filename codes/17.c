#include <stdio.h>
int main(){
int n;
printf("enter number");
scanf("%d",&n);
int fact=1;
for(int i=1;i<=n;i++){
    fact=fact*i;

}
printf("final factorial is %d",fact);



//     for(int i=5;i<=50;i++){
// if(i%2 !=0){
//     printf("%d\n",i);

// }




//  }

return 0;
}