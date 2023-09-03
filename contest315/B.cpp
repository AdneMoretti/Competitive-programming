#include <iostream> 
#include <bits/stdc++.h>

using namespace std; 
int main(){
    int M, D;
    int soma=0; 
    vector<pair<int, int>> v;
    cin >> M; 
    for(int i=0;i<M;i++){
        cin >> D; 
        soma+=D; 
        pair<int, int> par; 
        par.first = i+1;
        for(int j=1;j<=D;j++){
            par.second = j; 
            v.push_back(par);
        }
    }
    soma = soma/2; 
    cout << v[soma].first <<" "<< v[soma].second << endl;
    return 0; 
}