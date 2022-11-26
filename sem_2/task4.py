number = input()
rem = 0
temp = 10
num = int(number)
for i in range(len(number)):
    rem = num % 10
    if rem < temp:
        temp = rem
        num//=10
        if num == 0: print('yes')
    else: 
        print('no')
        break
    
