#include <stdio.h>
int main()
{
	long long int n,r,sum=0,i;
	long long int a;
	scanf("%lld",&n);
	for(i=1;i<=n;i++)
	{sum=0;
		scanf("%lld",&a);
		while(a!=0)
		{
			if(a%10==3)
			{
				sum=sum+1;
			}
			else {sum=sum;}
			a=a/10;
		}
		printf("%lld\n",sum);
	}
	return 0;
}

