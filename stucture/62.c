#include <stdio.h> 
 struct car { 
    char name[30]; 
    int price; 
}; 
 void print_car_info(struct car c) 
{ 
    printf("Name : %s", c.name); 
    printf("\nPrice : %d\n", c.price); 
} 
 int main() 
 
{ 
    struct car c = { "Tata", 1021 }; 
    print_car_info(c); 
    return 0;
}