#include<stdio.h>

int main(){
    float a, b;
    scanf("%f %f", &a, &b);

    if(b / a >= 1 && b / a <= 6){
        printf("Yes");
    }
    else{
        printf("No");
    }
}