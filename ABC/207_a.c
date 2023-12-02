#include<stdio.h>

int main(){
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);

    int ans1 = a + b;
    int ans2 = b + c;
    int ans3 = c + a;

    if(ans1 >= ans2 && ans1 >= ans3){
        printf("%d", ans1);
    }
    else if(ans2 >= ans1 && ans2 >= ans3){
        printf("%d", ans2);
    }
    else if(ans3 >= ans1 && ans3 >= ans2){
        printf("%d", ans3);
    }
}