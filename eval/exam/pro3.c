#include<stdio.h>
#include<string.h>
int main(){
    int i=0,num,x=0;
    scanf("%d",&num);
    while(x<num){
    char str[300];
    while((scanf("%s",str)) != EOF)
    {}
    for(i=0;i<strlen(str);i++)
    {
        if(str[i] >= 'a' && str[i]<= 'z' )
                str[i] -= 32;
    }
    printf("%s\n",str);
    x++;
    }
    return 0;
}
