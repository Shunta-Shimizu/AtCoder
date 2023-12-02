#include<stdio.h>

int main(){
    int x, y;
    scanf("%d %d", &x, &y);

    if(x < y){
        if(x+3 > y){
            printf("Yes");
        }
        else{
            printf("No");
        }
    }
    else if(x > y){
        if(x < y+3){
            printf("Yes");
        }
        else{
            printf("No");
        }
    }
}