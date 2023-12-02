#include<stdio.h>

int main(void){
    int n;
    char S[8];
    scanf("%d", &n);
    scanf("%s", S);
    
    if(S[n-1] == 'x'){
        printf("No");
    }
    else{
        printf("Yes");
    }
}
