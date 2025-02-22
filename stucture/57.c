#include<stdio.h>
#include<string.h>

typedef struct computerengineeringstudent
{
    int roll;
    float cgpa;
    char name[100];
  }coe;

  int main(){
    
  coe s1;
  s1.roll=2003;
  s1.cgpa=9.6;
  strcpy(s1.name,"govind");
  printf("student name is %s\n",s1.name);
  printf("student roll is %d\n",s1.roll);
  printf("student cgpa is %f\n",s1.cgpa);

  return 0;
  }
