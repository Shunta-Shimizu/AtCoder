#include<stdio.h>

int main(){
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);

    int ans = (7 - a) + (7 - b) + (7 - c);
    printf("%d", ans);
}