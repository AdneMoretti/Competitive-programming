#include <stdio.h>

int main(){
    int N;
    char c;
    int Poor=0;
    int Good=0;
    scanf("%d", &N);
    for(int i=0;i<=N;i++){
        scanf("%c", &c);
        if(c=='o'){
            Good++;
        }
        if(c=='x'){
            Poor++;
        }
    }
    if(Good>0 && Poor==0){
        printf("Yes\n");
    }
    else{
        printf("No\n");
    }

}