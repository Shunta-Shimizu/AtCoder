#include<stdio.h>

int main(){
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);

    if(a != b && b != c && c != a){
        printf("%d", 0);
    }
    else{
        if(a == b){
            printf("%d", c);
        }
        else if(a == c){
            printf("%d", b);
        }
        else if(b == c){
            printf("%d", a);
        }
    }
}