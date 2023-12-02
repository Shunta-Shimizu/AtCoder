#include<stdio.h>

int main(){
    int m, h;
    scanf("%d %d", &m, &h);

    if(h % m == 0){
        printf("Yes");
    }
    else{
        printf("No");
    }
}