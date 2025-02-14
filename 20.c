#include<stdio.h>

void RAMRAM();
void bonjour();
int main(){
printf("enter f for french & i for indian:");
char ch;
scanf("%c",&ch);
if(ch=='i'){
    RAMRAM();
    } else{
        bonjour();
    }
return 0;


}
void RAMRAM(){
    printf("RAMRAM\n");
}
void bonjour(){
    printf("bonjour\n");

}




    