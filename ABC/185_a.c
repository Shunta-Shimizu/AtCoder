#include<stab.h>

int main(){
    int A[4];
    for(int i; i<4; i++){
        scanf("%d", &A[i]);
    }

    int min = A[0];
    for(int i=1; i<4; i++){
        if(A[i] < min){
            min = A[i];
        }
    }

    printf("%d", min);
}