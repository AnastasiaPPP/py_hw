# 3) Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором.
from random import randint

lst = [randint(1, 41) for _ in range(30)]
print(lst)

def sort_list(lst):
    for i in range(len(lst) - 1):
        min = i
        for k in range(i + 1, len(lst)):
            if lst[k] < lst[min]:
                min = k
        lst[i], lst[min] = lst[min], lst[i]
    return lst

print(sort_list(lst))

