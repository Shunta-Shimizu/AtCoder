#include<stdio.h>
#include<math.h>

int main(){
    int a;
    scanf("%d", &a);

    int ans = a + pow(a, 2) + pow(a, 3);
    printf("%d", ans);
}