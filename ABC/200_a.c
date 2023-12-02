#include<stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    int ans = n / 100;

    if(n % 100 == 0){
        printf("%d", ans);
    }
    else{
        printf("%d", ans+1);
    }
}