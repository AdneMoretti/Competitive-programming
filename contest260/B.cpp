#include <iostream> 
#include <bits/stdc++.h> 

using namespace std; 
int main(){
    int n, x, z, y, a, b;
    vector <int> math; 
    vector<int> english; 
    vector<int> all; 
    cin >> n >> x >> y >> z; 
    for(int i=0;i<n;i++){
        cin >> a; 
        cin >> b; 
        math.push_back(a); 
        english.push_back(b); 
    }
    make_heap(math.begin(), math.end()); 
    make_heap(english.begin(), english.end()); 
    for(int i=0;i<x;i++){
        pop_heap(math.begin(), math.end());
    }

}