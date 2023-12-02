#include<stdio.h>

int main(){
    char C[3];
    scanf("%s", C);
    if(C[0] == C[1] && C[1] ==  C[2] && C[2] == C[0]){
        printf("Won");
    }
    else{
        printf("Lost");
    }
}