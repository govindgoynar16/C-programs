#include<stdio.h>
#include<string.h>
struct student{
    int roll;
   float cgpa;
   char name[100];
};
int main(){
    struct student s1;
    s1.roll = 2402735;
    s1.cgpa=8.04;
    strcpy(s1.name, "govind");

    printf("student name=%s\n",s1.name);
    printf("student roll=%d\n",s1.roll);
    printf("student cgpa=%f\n",s1.cgpa);
 
    struct student s2;
    s2.roll = 2402736;
    s2.cgpa=8.5;
    strcpy(s2.name, "mahipal");

    printf("student name=%s\n",s2.name);
    printf("student roll=%d\n",s2.roll);
    printf("student cgpa=%f\n",s2.cgpa);
 
    struct student s3;
    s3.roll = 2402737;
    s3.cgpa=7.5;
    strcpy(s3.name, "diwakar");

    printf("student name=%s\n",s3.name);
    printf("student roll=%d\n",s3.roll);
    printf("student cgpa=%f\n",s3.cgpa);
 
return 0;


}