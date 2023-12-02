#include<stab.h>

int main(){
    int a, b;
    int c, d;
    scanf("%d %d", &a, &b);
    scanf("%d %d", &c, &d);

    int ans = a * d - b * c;
    printf("%d", ans);
}