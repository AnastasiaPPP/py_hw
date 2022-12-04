def find_sum(l):
    summ = 0
    for i in range(len(l)):
        if i % 2 != 0:
            summ += l[i]
    return summ
print(find_sum(list(map(int, input().split()))))
