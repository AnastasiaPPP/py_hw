x = int(input('Input x: '))
y = int(input('Input y: '))

if x == 0 or y == 0:
    print('Не корректные данные')
elif x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
else:
    print('4')