#include<stdio.h>
void main()
{
	int j=1;
	long long int min;
long long int n,i;
	scanf("%d",&n);
	scanf("%d",&i);
	min=i;
	while(j!=n-1)
	{
		j++;
		scanf("%d",&i);
		if(i<min)
		{
			min=i;
		}
	}
	printf("%lld\n",min);
}
