
#include <bits/stdc++.h>

using namespace std;
using ll = long long;


int main(){
    ll N, res = 1;
    cin >> N;
    for(int i=N-1; i > 1;i--){
        res *= i;
    }
    cout << res << endl;
    return 0;
}
