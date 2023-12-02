#include<stdio.h>
#include<string.h>

int main(){
    char S[16];
    scanf("%s", S);
    char T[12] = "Hello,World!";
    int ls = strlen(S);
    int lt = strlen(T);
    if(ls < 12){
        printf("WA");
        return 0;
    }

    for(int i=0; i<ls; i++){
        if(S[i] != T[i]){
            printf("WA");
            return 0;
        }
    }
    printf("AC");
}