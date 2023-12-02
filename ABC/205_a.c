#include<stdio.h>

int main(){
    float a, b;
    scanf("%f %f", &a, &b);

    float ans = b / 100 * a;
    printf("%f", ans);
}