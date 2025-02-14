#include <stdio.h>

int main(){
    int math,science;
    printf("enter the math score:");
    scanf("%d", &math);
    
    printf("enter the science score:");
    scanf("%d", &science);

    if (math>=70 && science>=75){
        printf("student passes both the exam.gift $45\n");
        }
else if(math>=70){
    printf("student pass in math exam.gift $15\n");
    }
else if(science>=75){
    printf("student pass in science exam.gift $15\n");
} else {
    printf("the student fails in math and science");
}
return 0;
}