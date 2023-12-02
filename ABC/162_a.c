#include<stdio.h>

int main(){
    char N[3];
    scanf("%s", N);

    if(N[0] == '7' || N[1] == '7' || N[2] == '7'){
        printf("Yes");
    }
    else{
        printf("No");
    }
}