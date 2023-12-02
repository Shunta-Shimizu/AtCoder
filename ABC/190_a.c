#include<stdio.h>

int main(){
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);

    if(a > b){
        printf("Takahashi");
    }
    else if(a == b){
        if(c == 0){
            printf("Aoki");
        }
        else{
            printf("Takahashi");
        }
    }
    else{
        printf("Aoki");
    }
}