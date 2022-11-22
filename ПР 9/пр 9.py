a=[]
x=0
z=0
with open('D:\НазаровЯА_УБ_22_vvod.txt','r') as f:
    for line in f.readlines():
        b=line.replace('\n','').split()
        for i in range(len(b)):
            b[i]=int(b[i])
        a.append(b)
    print(a)
    print('Исходная матрица: ')
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],' ',end='')
    print()
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i][j] <= 0:
            continue
        if a[i][j] > 0:
            z += a[i][j]
            x+=1
print('Сумма:', z)
print('Число:', x)
with open('D:\НазаровЯА_УБ_22_vivod.txt','w') as t:
    t.write('Сумма элеменов: '+ " " + str(z) + '\n')
    t.write('Число: '+ " " + str(x) + '\n')
