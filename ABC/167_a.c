#include<stdio.h>
#include<string.h>

int main(){
    char S[11];
    char T[11];
    scanf("%s", S);
    scanf("%s", T);

    int ls = strlen(S);
    int lt = strlen(T);

    for(int i=0; i < ls; i++){
        if(S[i] != T[i]){
            printf("No");
            return 0;
        }
    }

    printf("Yes");
}