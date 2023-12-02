#include<stdio.h>

int main(){
    int x;
    scanf("%d", &x);

    if(x < 0){
        printf("%d", 0);
    }
    else{
        printf("%d", x);
    }
}