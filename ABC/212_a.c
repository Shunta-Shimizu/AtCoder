#include<stdio.h>

int main(){
    int a, b;
    scanf("%d %d", &a, &b);

    if(0 < a && b == 0){
        printf("Gold");
    }
    else if(a == 0 && 0 < b){
        printf("Silver");
    }
    else if(0 < a && 0 < b){
        printf("Alloy");
    }
}