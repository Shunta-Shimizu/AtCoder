#include<stdio.h>

int main(){
    int n;
    scanf("%d", &n);

    if(1 <= n && n <= 125){
        printf("%d", 4);
    }
    else if(126 <= n && n <= 211){
        printf("%d", 6);
    }
    else{
        printf("%d", 8);
    }
}