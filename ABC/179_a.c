#include<stdio.h>
#include<string.h>

int main(){
    char S[1000];
    scanf("%s", S);

    int n = strlen(S);
    if(S[n-1] == 's'){
        printf("%ses", S);
    }
    else{
        printf("%ss", S);
    }
}