import math
x=float(input ("x="))
y=float(input ("y="))
z=float(input ("z="))
s=((math.fabs(math.cos(x)-math.cos(y)))**(1+2*(math.sin(y)**2)))*(1+z+(z**2)/2+(z**3)/3+(z**4)/4)
print("s= {0:.5f}".format (s))
