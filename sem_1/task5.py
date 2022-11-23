import math

print('Введите коордиту А: ')
x = int(input('x = '))
y = int(input('y = '))

print('Введите коордиту B: ')
x1 = int(input('x = '))
y1 = int(input('y = '))

result = float('%.2f' % (math.sqrt((x - x1)**2 + (y - y1)**2)))
print(result)