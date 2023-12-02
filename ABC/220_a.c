#include<stdio.h>

int main(){
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    int i;
    for(i=a; i<=b; i++){
        if(i % c == 0){
            printf("%d", i);
            return 0;
        }
    }
    printf("%d", -1);
}