#include<stdio.h>

int main(){
    int a, b;
    scanf("%d %d", &a, &b);

    int a1 = a / 100;
    int a2 = a / 10 - 10 * a1;
    int a3 = a % 10;

    int b1 = b / 100;
    int b2 = b / 10 - 10 * b1;
    int b3 = b % 10;

    int ans1 = a1 + a2 + a3;
    int ans2 = b1 + b2 + b3;

    if(ans1 >= ans2){
        printf("%d", ans1);
    }
    else{
        printf("%d", ans2);
    }
}