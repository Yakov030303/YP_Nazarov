import math

def NOD (a,b):
	while a>0 and b>0:
		  q=int(max(a,b)/min(a,b))
		  if a>=b: 
			  a=a-b*q
		  else: 
			  b=b-a*q
	if(a>0):return a
	else: return b
	
    
	

a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
d=int(input("d= "))
a=a*d
b=b*c
q=int(NOD(a,b))
a=int(a/q)
b=int(b/q)
print (a)
print (b)