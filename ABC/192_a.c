#include<stdio.h>

int main(){
    int x;
    scanf("%d", &x);

    int y = x / 100 + 1;

    int ans = 100 * y - x;
    printf("%d", ans);
}