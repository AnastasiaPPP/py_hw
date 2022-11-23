day = int(input('Enter the number: '))

if day < 1 or day > 7:
    print('ERROR')
elif day == 6 or day == 7:
    print('yes')
else:
    print('no')