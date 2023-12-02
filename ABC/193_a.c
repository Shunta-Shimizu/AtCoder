#include<stdio.h>

int main(){
    float a, b;
    scanf("%f %f", &a, &b);

    float ans = (a - b) / a * 100;
    printf("%f", ans);
}