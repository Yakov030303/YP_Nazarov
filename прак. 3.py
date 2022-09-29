import math
k=int(input("k = "))
v=int(input("v = "))
if k<v : 
    s=v-k+1
elif k>v :
    s=k*k-v*v
else :
    s=k*k-k
print("s= {0:.5f}".format (s))
