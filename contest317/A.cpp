#include <iostream> 
#include <bits/stdc++.h>

using namespace std; 

int main(){
    int N, H, X, P; 
    int verifica = -1; 
    cin >> N >> H >> X; 
    for(int i=0;i<N;i++){
        cin >> P;
        if(H+P >= X and verifica == -1){
            verifica = i+1; 
        }
    }
    cout << verifica << endl;
}