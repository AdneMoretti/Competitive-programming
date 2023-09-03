#include <iostream>
#include <bits/stdc++.h> 

using namespace std; 

int main(){
    string s; 
    cin >> s;
    int one, two, three;
    one = two = three = 0;  
    for(auto i: s){
        if(i==s[0]){ 
            one++; 
        }
        if(i==s[1]){
            two++; 
        }
        if(i==s[2]){
            three++; 
        }
    }
    if(one==1){
        cout << s[0] << endl; 
    }
    else if(two==1){
        cout << s[1] << endl; 
    }
    else if(three==1){ 
        cout << s[2] << endl;
    }
    else{
        cout << "-1" << endl; 
    }
    return 0;

}