#include<stdio.h>
#include<math.h>
float squarearea(float side);
float circlearea(float rad);
float rectangulararea(float a, float b);


int main(){
float a=5.0;
float b=10.0;

printf("area is:%f",rectangulararea(a,b));
return 0;
}
// int n=4;
// printf("%f",pow(n,2));
// return 0;
float squarearea(float side){
    return side*side;
    }

float circlearea(float rad){
    return 3.14*rad*rad;

}
float rectangulararea(float a, float b){
    return a*b;
}

