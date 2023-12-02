#include<stdio.h>

int main(){
    int a, b;
    scanf("%d %d", &a, &b);

    int ans = 2 * a + 100 - b;
    printf("%d", ans);
}