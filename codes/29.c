#include<stdio.h>
int calpercentage(int science,int math, int sanskrit);
int main(){
int sc=98;
int math=95;
int sanskrit=97;

printf("percentage is :%d",calpercentage(sc,math,sanskrit));


    return 0;
}
int calpercentage(int science, int math, int sanskrit){
return ((science+math+sanskrit)/3);
}