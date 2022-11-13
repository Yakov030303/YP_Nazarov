x = []
sr = 0
n = int(input('Введите длину массива: '))
x = [float(input()) for i in range(n)]
for i in range(n):
    sr=sr+x[i]
sr=sr/n
for i in range(n):
    if x[i]<1:
        x[i]=sr
    print(x)