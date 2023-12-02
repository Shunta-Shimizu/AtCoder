#include<stdio.h>

int main(){
    int A[3];
    for(int i=0; i<3; i++){
        scanf("%d", &A[i]);
    }

    for(int i=0; i < 3; i++){
        for(int j=i+1; j < 3; j++){
            if(A[i] > A[j]){
                int tmp = A[i];
                A[i] = A[j];
                A[j] = tmp;
            }
        }
    }

    if(A[2] - A[1] == A[1] - A[0]){
        printf("Yes");
    }
    else{
        printf("No");
    }
}