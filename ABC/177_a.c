#include<stdio.h>

int main(){
    float d, t, s;
    scanf("%f %f %f", &d, &t, &s);

    if(d / s <= t){
        printf("Yes");
    }
    else{
        printf("No");
    }
}