#include<stdio.h>
int main(){
    long long n,min,num;
    scanf("%lld",&num);
    long long int i;
    for(i=0;i<num;i++){
        scanf("%lld",&n);
        if(i==0)
            min=n;
        else if(min>n)
            min = n;
    }
    printf("%lld\n",min);
   return 0;
}