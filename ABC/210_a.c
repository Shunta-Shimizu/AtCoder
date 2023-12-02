#include<stdio.h>

int main(){
    int n, a, x, y;
    scanf("%d %d %d %d", &n, &a, &x, &y);

    int ans = 0;
    for(int i=1; i<=n; i++){
        if(i >= a+1){
            ans += y;
        }
        else{
            ans += x;
        }
    }
    printf("%d", ans);
}