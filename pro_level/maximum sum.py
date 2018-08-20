N=int(input())
{
a=[]
for i in range(0,N):
  {
  b=int(input())
  a.append(b)
  }
print(a)
{
  s1=a[::2]
s2=a[1::2]
if(sum(s1)>sum(s2)):
  print(sum(s1))
else:
  print(sum(s2))
  }
}
