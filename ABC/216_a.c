#include<stdio.h>

int main(){
    double xy;
    scanf("%lf", &xy);
    int y = 10 * (xy - (int)xy);
    int x = (int)xy;

    if(0 <= y && y <= 2){
        printf("%d-", x);
    }
    else if(3 <= y && y <= 6){
        printf("%d", x);
    }
    else{
        printf("%d+", x);
    }
}