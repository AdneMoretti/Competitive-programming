#include <iostream>
#include <vector>
#include <string>

using namespace std;

long long fast_exp(long long a, int n, int Mod){
    long long res = 1, base = a%Mod;

    while (n){
        if(n & 1) 
            res = (res * base)% Mod;
        base = (base * base) % Mod;
        n >>= 1;
    }
    return res;
}

int main() {
    long long Mod, B, P, exponential;
    string line;
    while(cin >> B >> P >> Mod) {
        exponential = fast_exp(B, P, Mod);
        cout << exponential << endl;
    }
    return 0;
}