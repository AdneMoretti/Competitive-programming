#include <iostream> 
#include <bits/stdc++.h> 

using namespace std;
int main(){
    int N, M, number, menor, menor_number; 
    cin >> N >> M; 
    cin >> number;
    menor = number % M;
    menor_number = number;
    for(int i=0;i<N-1;i++){
        int number;
        cin >> number;
        if(number%M < menor){
            menor = number%M;
            menor_number=number;
        }
        else if(number%M == menor and number > menor_number){
            menor = number%M;
            menor_number=number;
        }
    }
    cout << menor_number << endl;
}