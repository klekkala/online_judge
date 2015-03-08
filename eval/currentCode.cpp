#include<stdio.h>
#include<iostream>
#include<string>
using namespace std;
#include<queue>
int main()
{
int test;
scanf("%d",&test);
while(test--)
{
	queue<string> q1;

	q1.push("1");
	int n;
scanf("%d",&n);
	string s1,s2;

	for(int i=1; i<=n; i++)
	{		
		s1 = s2 = q1.front();
		cout<<s1<<" ";
		printf("\n");
		q1.pop();
		s1.append("0");
		s2.append("1");
		q1.push(s1); q1.push(s2);
	}
}
	return 0;
}
