#include <stdio.h>
void main() 
{
	int n,i,j;
	int a[10];
	
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d ",&a[i]);
	}
	for(i=0;i<n;i++)
	{
	int x=0;	
		for(j=0;j<n;j++)
		{
			if(a[i]==a[j] && i!=j)
			{
				x=x+1;	
			}
			
		}
	if(x==0)
	{
		printf("%d",a[i]);
	}
	}

}
