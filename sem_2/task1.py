x = int(input())
y = int(input())
if x > y: y = x
count_of_digits = 0
for i in range(x, y + 1):
    if i % 2 == 0 and i % 3 == 0:
        count_of_digits += 1
print(count_of_digits)
