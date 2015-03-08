#include<stdio.h>
int main(){
    int n;
    scanf("%d",&n);
    int i;
    long long int arr[10000000];
    for(i=0;i<n;i++){
        scanf("%lld",&arr[i]);
    }
    long long int min=arr[0];
    for(i=0;i<n;i++){
        if(min>arr[i])
            min = arr[i];
    }
    printf("%lld\n",min);
    return 0;

}
