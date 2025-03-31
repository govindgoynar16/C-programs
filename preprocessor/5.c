#include<stdio.h>
#include<stdlib.h>
#define INTEL

int main(){
#ifdef INTEL
printf("code for INTEL machines\n");
#else
printf("code for non INTEL machines\n");
#endif //intel

#undef INTEL

#ifdef INTEL
printf("code for INTEL machines\n");
#else
printf("code for non INTEL machines");
#endif //intel

    return 0;
}