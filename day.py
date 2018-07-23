#include<stdio.h>
int main()
{
char a[100]=('mon','tue','wed','thur','fri','sat'),b[40];
scanf("%s",&b);
if(a==b)
{
printf("holiday");
}
else
{
printf("not");
}
return 0;
}
