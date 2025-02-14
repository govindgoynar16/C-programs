#include<stdio.h>
int main(){

    char ch;
    
    // Input from user
    printf("Enter a character: ");
    scanf("%c", &ch);
    
    // Check if the character is a digit
    if (ch >= '0' && ch <= '9') {
        printf("The character '%c' is a digit.\n", ch);
    } else {
        printf("The character '%c' is not a digit.\n", ch);
    }


return 0;

}