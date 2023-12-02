#include<stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    
    int p = n * 1.08;

    if(p < 206){
        printf("Yay!");
    }
    else if (p == 206){
        printf("so-so");
    }
    else{
        printf(":(");
    }
    
}