from random import randint

field = [i for i in range(1, 10)]

def print_field(f):
    for i in range(len(f)):
        if i % 3 == 0:
            print()
        print(f[i], end= '' + '  |  ' )
    print()

def your_turn(f):
    print('Ваш ход')
    print('Выберите  ячейку')
    cell = int(input())
    print('Ставим крестик :)')
    index = f.index(cell)
    f[index] = 'X'
    print_field(f)
    return f

def computer_turn(f):
    print('Мой ход!')
    print('Выбираю ячейку...')
    while True:
        cell = randint(0, 8)
        if f[cell] == 'X' or f[cell] == 'O':
            cell = randint(0, 8)
        else:
            f[cell] = 'O'
            break
    print_field(f)
    return f

def check_field(f):
    if (f[0] == 'X' and f[1] == 'X' and f[2] == 'X') or (f[0] == 'O' and f[1] == 'O' and f[2] == 'O'):
        return False
    elif (f[3] == 'X' and f[4] == 'X' and f[5] == 'X') or (f[3] == 'O' and f[4] == 'O' and f[5] == 'O'):
        return False
    elif (f[6] == 'X' and f[7] == 'X' and f[8] == 'X') or (f[6] == 'O' and f[7] == 'O' and f[8] == 'O'):
        return False
    elif (f[0] == 'X' and f[4] == 'X' and f[8] == 'X') or (f[0] == 'O' and f[4] == 'O' and f[8] == 'O'):
        return False
    elif (f[2] == 'X' and f[4] == 'X' and f[6] == 'X') or (f[2] == 'O' and f[4] == 'O' and f[6] == 'O'):
        return False
    elif (f[0] == 'X' and f[3] == 'X' and f[6] == 'X') or (f[0] == 'O' and f[3] == 'O' and f[6] == 'O'):
        return False
    elif (f[1] == 'X' and f[4] == 'X' and f[7] == 'X') or (f[1] == 'O' and f[4] == 'O' and f[7] == 'O'):
        return False
    elif (f[2] == 'X' and f[5] == 'X' and f[8] == 'X') or (f[2] == 'O' and f[5] == 'O' and f[8] == 'O'):
        return False
    else:
        return True

    
while True:
    computer_turn(field)
    if not check_field(field):
        print('Computer win')
        break
    your_turn(field)
    if not check_field(field):
        print('You win')
        break
    str_field = ''.join(str(field))
    if str_field.isalpha():
        print('Все ячейки закончились :( \n Ничья!')
        break

        




