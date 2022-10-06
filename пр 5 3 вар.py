s = input()
s = list(s)
print(s)

print('------')
print(len(s),' длина')

flag = 0
c = 0
while flag != len(s):
    if s[flag] == '.':
        s.remove('.')
        c +=1
    else:
        flag +=1
        
print(c,'количество точек')
print(s.count('.'),'проверка на удалённые точки')







