# include<stdio.h>

int main(){
    int a, b;
    scanf("%d %d", &a, &b);
    int ans = 1;
    for(int i=0; i<a-b; i++){
        ans *= 32;
    }
    printf("%d", ans);
} 