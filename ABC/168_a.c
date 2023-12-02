#include<stdio.h>
#include<string.h>

int main(){
    char N[3];
    scanf("%s", N);

    int i = strlen(N);
    if(N[i-1] == '0' || N[i-1] == '1' || N[i-1] == '6' || N[i-1] == '8'){
        printf("pon");
    }
    else if(N[i-1] == '3'){
        printf("bon");
    }
    else{
        printf("hon");
    }
}