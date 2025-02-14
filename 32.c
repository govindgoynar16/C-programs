  #include<stdio.h>
  void square(int n);
  void _square(int *n);
  int main(){
// float price=100.00;
// float *ptr=&price;
// float **pptr=&ptr;
// int i=5;
// int*ptr=&i;
// int **pptr=&ptr;
// printf("%d\n",**pptr); 
int number=4;
square(number);
printf("number=%d\n",number);
_square(&number);
printf("number=%d\n",number);


return 0;
  }
  //call by value
  void square(int n){
    n=n*n;
    printf("sqaure=%d\n",n);
  }
  void _square(int *n){
    *n=(*n)*(*n);
    printf("square=%d\n",*n);
  }