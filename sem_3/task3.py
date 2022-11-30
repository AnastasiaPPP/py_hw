text = input()
if text.count('о') >= 2:
    indexes = []
    for index, letter in enumerate(text):
        if letter == 'о':
            indexes.append(index)
    cut_text = text[indexes[0]:indexes[len(indexes) - 1]]
    new_str = ''.join(reversed(cut_text))
    new_str = text[:indexes[0] + 1] + new_str + text[indexes[len(indexes)-1] + 1:]
    print(new_str)
else:
    print('в слове одна буква "о" или их нет')