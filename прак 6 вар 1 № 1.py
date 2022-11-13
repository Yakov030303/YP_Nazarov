x = []
n = int(input('Введите длину массива: '))
x = [int(input()) for i in range(n)]
print(x)
z = max(x)
print('Максимальный элемент массива: ', z)
x.reverse()
print('Развернутый список: ', x)