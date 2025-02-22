#include<stdio.h>
#include<string.h>
struct student{
int roll;
float cgpa;
char name[100];
};
int main(){
    struct student s1={1664,8.5,"govind"};
// printf("student roll=%d\n",s1.roll);
// printf("student cgpa=%f\n",s1.cgpa);
// printf("student name=%s\n",s1.name);


//pointer method
struct student*ptr=&s1;

// printf("student roll=%d\n",(*ptr).roll);
// printf("student cgpa=%f\n",(*ptr).cgpa);
// printf("student name=%s\n",(*ptr).name);

printf("student->roll=%d\n",ptr->roll);
printf("student->cgpa=%f\n",ptr->cgpa);
printf("student->name=%s\n",ptr->name);

//array of structure
// struct student ece[100];
    // ece[0].roll=25;
    // ece[0].cgpa=8.9;
    // strcpy(ece[0].name,"shradha");
    // printf("name=%s\n",ece[0].name);
    // printf("name=%d\n",ece[0].roll);
    // printf("name=%f\n",ece[0].cgpa);

return 0 ;
}