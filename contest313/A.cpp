#include <iostream> 
#include <bits/stdc++.h> 


using namespace std; 
int main(){
    int N; 
    vector<int> numbers; 
    int P, Pi; 
    cin >> N >> P; 
    for(int i=1;i<N;i++){
        cin >> Pi; 
        numbers.push_back(Pi); 
    }
    if(N>1){    
        sort(numbers.rbegin(), numbers.rend()); 
        if(numbers[0]==P){
            cout << "1" << endl;
        }
        else if(P>numbers[0]){
            cout << "0" << endl;
        }
        else{
            cout << numbers[0] - P + 1 << endl; 
        }
    }
    else{
        cout << "0" << endl;
    }


}