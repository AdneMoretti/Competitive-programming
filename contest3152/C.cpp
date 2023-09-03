#include <iostream> 
#include <bits/stdc++.h> 

using namespace std;
using ll = long long; 

int solve(int n){ 
    ll F, S, maior, number; 
    maior = 0;
    number = 0;
    vector<pair<int, int>> flavors; 
    for(int i=0;i<n;i++){
        cin >> F >> S; 
        for(auto i: flavors){
            if(F == i.first){
                if(S >= i.second){
                    number = S + i.second/2;
                }
                else{
                    number =  i.second + S/2;         
                }
            }
            else{
                number =  S + i.second; 
            }
            if(number > maior){
                maior = number; 
            }
        }
        flavors.push_back(make_pair(F, S));
    }
    return maior; 
}

int main(){
    int N;
    cin >>  N; 
    cout << solve(N) << "\n"; 
}