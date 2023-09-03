#include <iostream> 
#include <bits/stdc++.h> 

using namespace std;
int solve(){
    int N, B;
    cin >> B >> N;
    float res = B;
    if(N>3){
        res += (N-3)*100;
        if(N > 7){
            res = ((res*50)/100) + res;
        }
        else{
            res = ((res*25)/100) + res;
        }

}
    return res;
}

int main(){
    int T;
    cin >> T;
    for(int i=0;i<T;i++){
        int res = solve();
        res == 1? cout << "Caso " << i+1 << ": " << res << " ponto" << endl : 
        
    }

    return 0;
}