n=int(input())
q=int(input())
li=[]
a=[]
for i in range(0,n):
	li.append(int(input()))
for i in range(0,q):
	s=0
	u=int(input())
	v=int(input())
	for i in range(u-1,v):
		s=s^li[i]
	a.append(s)
print(a)
