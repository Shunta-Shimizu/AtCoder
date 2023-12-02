#include<stdio.h>

int main(){
    int n;
    scanf("%d", &n);

    int m;
    if(n % 1000 == 0){
        m = n / 1000;
    }
    else{
        m = n / 1000 + 1;
    }
    int ans = 1000 * m - n;
    printf("%d", ans);
}