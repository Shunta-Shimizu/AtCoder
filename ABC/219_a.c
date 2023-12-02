#include<stdio.h>

int main(){
    int x;
    scanf("%d", &x);
    int res;
    if(0 <= x && x < 40){
        res = 40 - x;
        printf("%d", res);
    }
    else if(40 <= x && x < 70){
        res = 70 - x;
        printf("%d", res);
    }
    else if(70 <= x && x < 90){
        res = 90 - x;
        printf("%d", res);
    }
    else{
        printf("expert");
    }
}