#include<stdio.h>
int main()
{
	int a[10],i,j,m,t;
	scanf("%d",&m);
	for(i=1;i<=m;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=1;i<=m;i++)
	{
		for(j=1;j<=m;j++)
		{
			if(a[i]>a[j])
			{
			   t=a[i];
			   a[i]=a[j];
			   a[j]=t;
			}
		}
	}
	for(i=1;i<=m;i++)
	{
		printf("%d->",a[i]);
	}
	return 0;
}
