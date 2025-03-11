#include<stdio.h>
#include<string.h>
typedef struct bankaccount{
    char name[100];
    int accountno;
}acc;

int main(){
    acc acc1 = {123, "govind"};
    acc acc2 = {124, "shubh"};
    acc acc3 = {125, "diwakar"};

printf("acc no =%d",acc1.accountno);
printf("name =%c",acc1.name);

printf("acc no =%d",acc2.accountno);
printf("name =%c",acc2.name);


printf("acc no =%d",acc3.accountno);
printf("name =%c",acc3.name);



    return 0;
}