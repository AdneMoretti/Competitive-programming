#include <iostream> 
#include <bits/stdc++.h> 
#include <math.h>

using namespace std;

int main(){
    int L, HP, S, BS, IV, EV;
    vector<int> m;
    cin >> L;
    for(int i=0;i<4;i++){
        cin >> BS >> IV >> EV;
        if(i==0){
            m.push_back((((IV + BS + sqrt(EV)/8 + 50) * L)/50) +10);
        }
        else{
            m.push_back((((IV + BS + sqrt(EV)/8) * L)/50) +5);
        }
    }
    for (auto i: m){
        cout << i << endl;
    }
    return 0;
}