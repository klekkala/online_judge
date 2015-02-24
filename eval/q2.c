#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include<malloc.h>
//#include<iostream>
//using namespace std;
#define ROW 10000
#define COL 10000
struct node
{
	int vertex;
	struct node *next;
};
typedef struct node* nodeptr;
nodeptr getnode()
{
	nodeptr p;
	p=(nodeptr)malloc(sizeof(struct node));
	p->next=NULL;
	return p;
}
int visited[20000];
void init(nodeptr head[],int n)
{
	int v;
	for(v=1; v<=n; v++)
		head[v]=NULL;
}
void initialise_visit(int n)
{
	int i;
	for(i=1;i<=n;i++)
		visited[i]=0;
}
void DFSR(nodeptr head[],int start)
{

	nodeptr adj;
	visited[start]=1;
	// printf("\t %d",start);
	adj=head[start];
	while(adj!=NULL)
	{

		if(visited[adj->vertex]==0)
		{
			DFSR(head,adj->vertex);
		}
		adj=adj->next;
	}
}
int main()
{
	int t;
	scanf("%d",&t);
	while(t--)
	{
		int V,E;

		scanf("%d %d",&V,&E);
		nodeptr head[V];
		int i;
		int cnt=0;
		init(head,V);
		for(i=0; i<E; i++)
		{
			nodeptr new1,p;
			int a,b;
			scanf("%d %d",&a,&b);
			new1=getnode();
			new1->vertex=b;
			p=head[a];
			if(p==NULL)
				head[a]=new1;
			else
			{
				while(p->next!=NULL)
					p=p->next;
				p->next=new1;
			}
			new1=getnode();
			new1->vertex=a;
			p=head[b];
			if(p==NULL)
				head[b]=new1;
			else
			{
				while(p->next!=NULL)
					p=p->next;
				p->next=new1;
			}
		}

		initialise_visit(V);

		for(i=1;i<=V;i++)
			if(visited[i]==0)
			{
				DFSR(head,i);
				cnt++;
			}
		printf("%d\n",cnt);
	}
	return 0;
}

