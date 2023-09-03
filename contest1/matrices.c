#include <stdio.h>

int main(){
    int N;
    scanf("%d", &N);
    int A[100][100];
    int B[100][100];
    int b1;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            scanf("%d", &A[i][j]);
        }
    }
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            scanf("%d", &B[i][j]);
            if(B[i][j]==1){
                b1++;
            }
        }
    }
    for(int i=1;i<N;i++){
        for(int j=1;j<N;j++){
            A[i][j] = A[N+1-j][i];
        }
    }

}