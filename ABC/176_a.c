#include<stdio.h>

int main(){
    int n, x, t;
    scanf("%d %d %d", &n, &x, &t);

    int mt;
    if(n % x != 0){
        mt = (n / x + 1) * t;
    }
    else{
        mt = n / x * t;
    }
    printf("%d", mt);
}