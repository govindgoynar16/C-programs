// #include<stdio.h>
// int main(){
//     FILE*fptr;
// fptr=fopen("newtext.txt","r");

// int ch;
// fscanf(fptr,"%d\n",&ch);
// printf("character=%d\n",ch);
// fscanf(fptr,"%d\n",&ch);
// printf("character=%d\n",ch);
// fscanf(fptr,"%d\n",&ch);
// printf("character=%d\n",ch);

// fclose(fptr);
// return 0;
// }



// #include<stdio.h>
// int main(){
//     FILE*fptr;
// fptr=fopen("newtext.txt","w");

// fprintf(fptr,"%c",'m');
// fprintf(fptr,"%c",'a');
// fprintf(fptr,"%c",'n');
// fprintf(fptr,"%c",'g');
// fprintf(fptr,"%c",'o');
// fclose(fptr);
// return 0;
// }


// #include<stdio.h>
// int main(){
//     FILE*fptr;
// fptr=fopen("newtext.txt","w");
// fputc('m',fptr);
// fputc('a',fptr);
// fputc('n',fptr);
// fputc('g',fptr);
// fputc('o',fptr);

// printf("%c\n",fgetc(fptr));
// printf("%c\n",fgetc(fptr));
// printf("%c\n",fgetc(fptr));
// printf("%c\n",fgetc(fptr));
// printf("%c\n",fgetc(fptr));

// fprintf(fptr,"%c",'m');
// fprintf(fptr,"%c",'a');
// fprintf(fptr,"%c",'n');
// fprintf(fptr,"%c",'g');
// fprintf(fptr,"%c",'o');
// fclose(fptr);
// return 0;
// }

// #include<stdio.h>
// int main(){
//     FILE*fptr;
// fptr=fopen("newtext.txt","r");
// char ch;
// ch=fgetc(fptr);
// while(ch!=EOF){
//     printf("%c",ch);
//     ch=fgetc(fptr);
// }
// printf("\n");
// fclose(fptr);
// return 0;
// }