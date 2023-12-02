#include<stdio.h>

int main(){
    int a, b;
    int c, d;
    scanf("%d %d", &a, &b);
    scanf("%d %d", &c, &d);

    int ans = b - c;
    printf("%d", ans);
}