#include<stdio.h>

int main(){
    int k;
    int a, b;
    scanf("%d", &k);
    scanf("%d %d", &a, &b);

    for(int i=a; i <= b; i++){
        if(i % k == 0){
            printf("OK");
            return 0;
        }
    }
    printf("NG");
}