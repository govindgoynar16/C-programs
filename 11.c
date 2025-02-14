#include <stdio.h>
int main(){
char ch;
printf("enter character:");
scanf("%c",&ch);
if(ch>='A'&&ch<='Z'){
printf("upper case");
}
else if(ch>='a'&&ch<='z')
{
    printf("lower case");

}
else{
    printf("not a english letter");
}









// int x=2;
// if(x=1){
//     printf("x is equal to 1");
// }
// else{
//     printf("x is not equal to 1");
// }



    return 0;
}
