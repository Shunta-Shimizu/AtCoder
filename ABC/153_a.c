#include<stdio.h>

int main(){
    int h, a;
    scanf("%d %d", &h, &a);

    int ans = 0;
    while(h > 0){
        h -= a;
        ans ++;
    }

    printf("%d", ans);
}