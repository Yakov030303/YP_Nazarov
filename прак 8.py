import math
from xmlrpc.client import MAXINT
n=int(input("size arry = "))
x=[]
maxx=minn=maxi=mini=0
print("read in matrix")
for i in range(n):
      b=[]
      for j in range(n): 
          b.append(int(input()))
          if i==0 and j==1:maxx=minn=b[0]+b[1]
          if j>0:
              if b[j-1]+b[j]>maxx:
                  maxx=b[j-1]+b[j]
                  maxi=i
              if b[j-1]+b[j]<minn:
                  minn=b[j-1]+b[j]
                  mini=i
      x.append(b)

print("max summ = ",maxx)
for j in range(n): print(x[maxi][j],end=" ")
print();
print("min summ = ",minn)
for j in range(n): print(x[mini][j],end=" ")
print();
print("new matrix")
for i in range (n):
      for j in range(n):
          if x[i][j]<0 :x[i][j]=0
          else: x[i][j]=1
for i in range (n):
      for j in range(n):
          if i>=j: print (x[i][j],end=" ")
      print();