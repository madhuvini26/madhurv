#include<stdio.h>
void main()
{
    int n,k,a[10],b[10],i,j,l,t;
    printf("Enter N : ");
    scanf("%d",&n);
    printf("\nEnter K : ");
    scanf("%d",&k);
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    for(i=0;i<k;i++)
    {
        scanf("\t%d",&b[j]);
    }
    for(i=0;i<n;i++)
    {
            if(a[i]>b[j])
            {
                t=a[i];
            }
            else
            {
             t=b[i];
            }
    }
    printf("The Largest Number is %d",t);
     }
