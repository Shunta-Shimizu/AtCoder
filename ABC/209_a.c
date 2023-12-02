#include<stdio.h>

int main(){
    int a, b;
    scanf("%d %d", &a, &b);

    int ans = b - a;
    if(ans <= 0){
        printf("%d", 0);
    }
    else{
        printf("%d", ans+1);
    }
}