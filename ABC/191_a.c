#include<stdio.h>

int main(){
    float v, t, s, d;
    scanf("%f %f %f %f", &v, &t, &s, &d);

    if(d / v >= t && d / v <= s){
        printf("No");
    }
    else{
        printf("Yes");
    }
}