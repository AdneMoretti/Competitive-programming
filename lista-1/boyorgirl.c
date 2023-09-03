#include <stdio.h>

int find(char *v, char c){
    for(int j=0;v[j]!='\0';j++){
        if(c==v[j]){
            return 1;
        }
    }
    return 0;

}
int main(){
    char username[101];
    scanf("%s", username);
    char aux[101];
    int x=1;
    char c;
    aux[0] = scanf("%c", &c);
    for(int i=1;scanf("%c", &c)!='\0';i++){
        if(!find(aux, c)){
            aux[x++] = c;
        }
    }
    if(x%2==0){
        printf("CHAT WITH HER!\n");
    }
    else{
        printf("IGNORE HIM!\n");
    }
    return 0;
}