#include<stdio.h>

int main(){
    float a, b;
    scanf("%f %f", &a, &b);
    float c = (a - b) / 3 + b;
    printf("%f", c);
}