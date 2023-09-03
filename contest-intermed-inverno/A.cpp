#include <iostream> 
#include <bits/stdc++.h> 

using namespace std; 

int main(){
    string dad, mom; 
    string res = ""; 
    cin >> dad; 
    cin >> mom; 
    int maior_dad = dad[0];
    int i_maior_dad = 0;
    int maior_mom = mom[0]; 
    int i_maior_mom = 0; 
    for(int i=1; i<dad.size();i++){
        if(dad[i]>maior_dad){
            maior_dad = dad[i];
            i_maior_dad = i;
        }
        if(mom[i]>maior_mom){
            maior_mom = mom[i];
            i_maior_mom = i;
        }
    }
    for(int i = dad.size(); i < mom.size();i++){
        if(mom[i]>maior_mom){
            maior_mom = mom[i];
            i_maior_mom = i;
        }
    }
    res+= maior_dad;
    int k = i_maior_dad+1;
    while(k != dad.size()){
        if(dad[k] > maior_mom){
            res+=dad[k]; 
        }
        k++;
    }
    string new_mom = mom.erase(0, i_maior_mom);
    res += new_mom;
    cout << res << endl;
}