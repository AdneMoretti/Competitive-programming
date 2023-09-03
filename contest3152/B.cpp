#include <iostream> 
#include <bits/stdc++.h> 

using namespace std; 

int main(){
    int D, X, soma=0; 
    vector<pair<int, int>> pares; 
    cin >> D; 
    for(int i=0;i<D;i++){
        cin >> X;
        pares.push_back(make_pair(soma+1, soma+X));
        soma+=X; 
    }
    int meio = (soma+1)/2; 
    for(int i=0;i<=pares.size();i++){
        if(meio >= pares[i].first and meio <= pares[i].second){
            cout << i+1 << " " << meio - pares[i].first + 1 << endl; 
        }
    }
    return 0;
}