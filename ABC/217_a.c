#include<stdio.h>
#include<string.h>

int main(){
    char S[11];
    char T[11];
    scanf("%s %s", S, T);
    
    int i;
    int ls = strlen(S);
    int lt = strlen(T);

    int flag = 0;
    for(i=0; i<ls; i++){
        if(S[i] > T[i]){
            // printf("%c", S[i]);
            flag = 1;
            break;
         }
         else if(S[i] < T[i]){
            flag = 0;
            break;
         }
    }
    
    if(flag == 1){
        printf("No");
    }
    else{
        printf("Yes");
    }
}