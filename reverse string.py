#include<stdio.h>
#include<string.h>
int main()
{
    char s1[30],s2[20],s3,s4;
    scanf("%s %s",s1,s2);
    s3=strrev(s1);
    s4=strrev(s2);
    printf("%s",strconcat(s3,s4));
    return 0;
    
}
