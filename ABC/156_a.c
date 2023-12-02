#include<stdio.h>

int main(){
    int n, r;
    scanf("%d %d", &n, &r);

    int ans;
    if(n < 10){
        ans = r  + 100 * (10 - n);
    }
    else{
        ans = r;
    }
    printf("%d", ans);
}