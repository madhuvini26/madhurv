a=0
b=0
brackets=raw_input("Enter input")
length=len(brackets)
for i in range(0,length):
     if (brackets[i]==')'):
              a+=1
     elif (brackets[i]=='('):
              b+=1
if(a-b==0):
	     print "Yes"
else:
	     print  "No"
    
