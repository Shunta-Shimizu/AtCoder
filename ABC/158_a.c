#include<stdio.h>

int main(){
    char S[3];
    scanf("%s", S);

    if((S[0] == 'B' && S[1] == 'B' && S[2] == 'B')){
        printf("No");
    }
    else if(S[0] == 'A' && S[1] == 'A' && S[2] == 'A'){
        printf("No");
    }
    else{
        printf("Yes");
    }
}