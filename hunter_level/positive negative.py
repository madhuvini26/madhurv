a=int(input())
l=[]
for i in range(1,a+1):
  n=int(input())
  l.append(n)
print (l)
m=l[0]
for x in l:
  if (m+x==0):
print (m,x)
