from numpy import zeros
from random import randint

print('Задайте размеры игрового поля противника: ')
x, y = int(input()), int(input())
field = zeros([x, y])
print(f'Игровое поле: \n{field}')
print('Задайте размеры вашего поля')
x1, y1 = int(input()), int(input())
field_2 = zeros([x1, y1])
print(field_2)
x3, y3 = randint(0, x - 1), randint(0, y - 1)
field[x3][y3] = 1
print('Компьютер загадал ячейку в своем поле')
gamer_field = zeros([x, y])
print('Загадайте ячейку в своем поле: \n Строка: ')
x2 = int(input()) - 1
print('Столбец: ')
y2 = int(input()) - 1
gamer_field[x2][y2] = 1
print('*** НАЧИНАЕМ ИГРУ ***')
print()
    
def gamer_move(x3, y3):
    print('Ваш ход \n Введите номер строки ')
    row = int(input()) - 1
    print('Номер столбца ')
    column = int(input()) - 1
    if row == x3 and column == y3:
        print('Потопил!')
        return False
    elif row + 1 > x or column + 1 > y:
        print('Выход за границы игрового поля.')
        return True
    else:
        print('Мимо :(')
        return True

def comp_move(x1, y1):
    print('Ход компьютера. \n Выбираю ячейку ')
    row = randint(0, x1 - 1)
    column = randint(0, y1 - 1)
    if row == x2 and column == y2:
        print('Потопил!')
        return False
    elif row + 1 > x1 or column + 1 > y1:
        print('Выход за границы игрового поля.')
        return True
    else:
        print('Мимо :(')
        return True
        
while True:
    if not gamer_move(x3, x3):
        print('You win')
        break
    if not comp_move(x1, y1):
        print('computer win')
        break    
