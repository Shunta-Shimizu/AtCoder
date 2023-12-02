#include<stdio.h>
#include<string.h>

int main(){
    char S[11], T[11];
    int a, b;
    char U[11];
    scanf("%s %s", S, T);
    scanf("%d %d", &a, &b);
    scanf("%s", U);

    if(strcmp(S, U) == 0){
        printf("%d %d", a-1, b);
    }
    else if(strcmp(T, U) == 0){
        printf("%d %d", a, b-1);
    }
}