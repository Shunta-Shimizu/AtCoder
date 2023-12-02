#include<stdio.h>

int main(){
    int n;
    scanf("%d", &n);

    int ans;
    if(n % 2 == 0){
        ans = n / 2;
    }
    else{
        ans = n / 2 + 1;
    }
    printf("%d", ans);
}