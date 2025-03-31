#include<stdio.h>
#include<stdlib.h>
#define INDIA 1
#define US 2
#define PAK 3
#define OTHER 4


#define COUNTRY INDIA
// #define COUNTRY US
// #define COUNTRY PAK
// #define COUNTRY OTHER
#define AGE 18
int main(){
printf("code for the universe\n");

#if COUNTRY==INDIA
  printf("code for the indians\n");
  #if AGE>=18
    printf("i'm adult");
  #else
    printf("i'm minor");
  #endif
#elif COUNTRY==US
  printf("code for the US");
#elif COUNTRY==PAK
printf("code for the PAK");
#else 
printf("code for other countries");
#endif //country

 



    return 0;
}