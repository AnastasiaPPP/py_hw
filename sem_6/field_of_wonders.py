import ast
import random

dict_from_file = {}
with open('sem_6\questions.txt', 'r', encoding = 'utf-8') as text:
    str = text.read()
dict_from_file = ast.literal_eval(str)
dict_of_riddles = {v:k for k, v in dict_from_file.items()}

word = random.choice(list(dict_of_riddles.keys()))
question = dict_of_riddles[word]
question_word = ''.join('_' for _ in range(len(word)))
print(question)
print(question_word)

def move_of_player(word, quest_word):
    print()
    print('Ваш ход \n')
    letter = input('Буква: ')
    if letter in quest_word:
        print('Такая буква уже есть в слове!')
    start = 0
    for char in word:
        if char == letter:
            ind = word.find(letter, start)
            quest_word = quest_word[:ind] + letter + quest_word[ind + 1:]
            start = ind + 1
    return quest_word
            


def spin_reel(word, quest_word):
    reel = ['Сектор Приз', 'Сектор "+"', '50', '100', '150', '200', '250', '300', '350']
    print('Крутим барабан')
    spin = random.choice(reel)
    print(f'На барабане {spin}')
    if spin.isdigit():
        return int(spin)
    elif spin == 'Сектор Приз':
        print('Вы выиграли котика!')
        return print_cat()
    else:
        open_letter = int(input('Введите номер буквы, которую хотите открыть: '))
        letter = word[open_letter - 1]
        if word.count(letter) > 1:
            for char in word:
                if char == letter:
                    ind = word.index(char)
                    quest_word = quest_word[:ind] + letter + quest_word[ind + 1:]
                    print(quest_word)
                return quest_word
        else:
            ind = word.index(letter)
            quest_word = quest_word[:ind] + letter + quest_word[ind + 1:]
            print(quest_word)
            return quest_word

def move_of_computer(word, quest_word):
    print()
    print('Ход компьютера')
    alphabet = 'абвгдеёжзийклмопрстуфхцчшщъьыэюя'
    index = random.randint(0, len(alphabet) - 1)
    letter = alphabet[index]
    start = 0
    for char in word:
        if char == letter:
            ind = word.find(letter, start)
            quest_word = quest_word[:ind] + letter + quest_word[ind + 1:]
            start = ind + 1
    alphabet.replace(letter, '')
    return quest_word
    

def print_cat():
    with open('sem_6\cat.txt', 'r', encoding = 'utf-8') as cat:
        line = cat.read()
        for str in line:
            print(str, end= '')

def check_word(question_word):
    if '_' not in question_word:
        print('Конец игры!')
        return False
    else:
        return True

sum_of_points_of_gamer = 0
sum_of_points_of_computer = 0

while True:
    sp = spin_reel(word, question_word)
    if not check_word(question_word):
        break
    if type(sp) is int:
        sum_of_points_of_gamer += sp
        print(f'У вас {sum_of_points_of_gamer} очков')
    elif type(sp) is str:
        question_word = sp
        print(question_word)
    question_word =  move_of_player(word, question_word)
    print(question_word)
    if not check_word(question_word):
        break
    sp_2 = spin_reel(word, question_word)
    if type(sp_2) is int:
        sum_of_points_of_computer += sp_2
        print(f'У компьютера {sum_of_points_of_computer} очков')
    elif type(sp_2) is str:
        question_word = sp_2
    question_word = move_of_computer(word, question_word)
    print(question_word)
    if not check_word(question_word):
        break
