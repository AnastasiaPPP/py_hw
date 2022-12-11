import random

n = int(input('Сколько вам нужно паролей? '))
m = int(input('Какой длины должны быть пароли? '))

def generate_password(length):
    password = ''
    count = 0
    lower_letters = 'abcdefghjkmnpqrstuvwxyz'
    upper_letters = 'ABCDEFGHJKMNPQRSTUVWXYZ'
    digits = '123456789'
    while True:
        if count < length:
            password += random.choice(lower_letters)
            count += 1
        else: break
        if count < m:
            password += random.choice(upper_letters)
            count += 1
        else: break
        if count < m:
            password += random.choice(digits)
            count += 1
        else: break
    return password

def main(count):
    passwords_list = []
    while True:
        passwords_list.append(generate_password(m))
        if len(passwords_list) == count:
            break
    return passwords_list

print(main(n))