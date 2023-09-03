#include <iostream>
#include <math.h>

using namespace std;


int main(){
    long long int number, soma;
    while(cin >> number){
        soma = ((1+number)*number)/2;
        cout << soma*soma << "\n";
    }
    return 0;
}
