#include<stdio.h>

int main(){
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);

    if(a == b && b !=c && a != c){
        printf("Yes");
    }
    else if(a != b && a == c && b != c){
        printf("Yes");
    }
    else if(b == c && a != c && a != b){
        printf("Yes");
    }
    else{
        printf("No");
    }
}
