x = int(input())
temp = 0
max1 = 0
max2 = 0
for i in range(x):
    digit = int(input())
    if digit > max1 or digit > max2: 
        if digit > max1: max1 = digit
        else: max2 = digit
        
print(max1, max2)