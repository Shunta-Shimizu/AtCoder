#include<stdio.h>

int main(){
    char S[3];
    scanf("%s", S);

    if(S[0] == 'R' && S[1] == 'R' && S[2] == 'R'){
        printf("%d", 3);
    }
    else if(S[0] == 'R' && S[1] == 'R' && S[2] == 'S'){
        printf("%d", 2);
    }
    else if(S[0] == 'S' && S[1] == 'R' && S[2] == 'R'){
        printf("%d", 2);
    }
    else if(S[0] == 'S' && S[1] == 'S' && S[2] == 'S'){
        printf("%d", 0);
    }
    else{
        printf("%d", 1);
    }
}