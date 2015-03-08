#include<stdio.h>
#include<math.h>
int main()
{
	int k;
	scanf("%d",&k);
	while(k--)
	{
		int i,x,n;
		float sum=0,j;
		scanf("%d %d",&x,&n);
		for(i=0;i<=n;i++)
		{
			if(i==0)
			{
				sum=1;
			}
			else
			{
				float h=fact(i);
				float g=pow(x,i);
				j=h/g;
				if(i%2!=0)
				{
					j=-j;
				}
				sum=sum+j;
			}
		}
printf("%0.4f\n",sum);
	}
	return 0;
}
int fact(int j)
{
	if(j==0)
		return 1;
	else
		return j*fact(j-1);
}
