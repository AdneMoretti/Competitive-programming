#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    int A, B, C, K, L;
    int soma = 0;
    cin >> A >> B >> C >> K;
    L = K - A;
    if(L > 0){
        soma += A;
        L = L - B;
        if(L > 0){ 
            soma -= L;
        }
    }
    else{
        soma = K;
    }
    printf("%d\n", soma);
}