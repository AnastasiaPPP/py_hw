# 2) Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
# И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)

from random import randint
import numpy

a , b = int(input()), int(input())

def create_matrix (a, b):
    matr = numpy.empty([a, b])
    for i in range(a):
        for k in range(b):
            matr[i][k] = randint(1,11)
    return matr

matrix = create_matrix(a, b)
print(matrix)

def calc_sum (matr):
    for i in range(len(matr)):
        sum = 0
        for k in matr[i]:
            sum += k
        sum /= len(matr[0])
        print(f'среднеарифметическое {i + 1} строки = {sum}')


calc_sum(matrix)