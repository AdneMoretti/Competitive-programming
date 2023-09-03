
#include <stdio.h>
#include <math.h>

int main(){
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    if(abs(c-a)<=d){
        printf("Yes\n");
    }
    else if(abs(b-a)<=d && abs(c-b)<=d){
        printf("Yes\n");
    }
    else{
        printf("No\n");
    }


    return 0;
}