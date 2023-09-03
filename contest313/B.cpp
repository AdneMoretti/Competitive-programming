#include <iostream> 
#include <bits/stdc++.h> 

using namespace std; 

int main(){
    int N, M; 
    cin >> N >> M; 
    vector<int> numbers; 
    vector<int> response; 
    for(int i=0;i<N;i++){
        numbers.push_back(0);
    }
    int A, B;
    for(int i=0; i<M;i++){
        cin >> A >> B; 
        numbers[B-1]++; 
    }

    for(int j=0;j<N;j++){
        if(numbers[j]==0){
            response.push_back(j+1);
        }
    }

    if(response.size()>1){
        cout << -1 << endl;
    }
    else{
        cout << response[0];
    }
}