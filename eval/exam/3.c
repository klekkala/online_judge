#include<stdio.h>

int main()
{
	int n,i,j,u;
	char c,a[301];
	scanf("%d",&n);
	u=n;
	c=getchar();
	while(n--)
	{
		i=0;
		while((a[i]=getchar())!=EOF)
		{
			if(a[i]>='a'&&a[i]<='z')
				a[i]=a[i]-32;	
			i++;
		}
		a[i]='\0';
		for(j=0;a[j]!='\0';j++)
		{
			printf("%c",a[j]);
		}
		printf("\n");
	}
	return 0;
}
