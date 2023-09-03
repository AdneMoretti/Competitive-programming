#include <iostream> 
#include <bits/stdc++.h> 

using namespace std;
// int solve(){
    
// }

int main(){
    float G, D, R, res;
    cin >> G >> D >> R;
    res =  (R / (1-D/100)) / (G/1000);
    cout << fixed;
    cout << setprecision(8);
    cout << res;
    return 0;
}