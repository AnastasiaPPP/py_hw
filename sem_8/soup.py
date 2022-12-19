ingridients = {'Капуста': 'Щи', 'Свекла': 'Борщ', 'Колбаса': 'Солянка', 'Грибы': 'Грибной суп', 'Рыба': 'Уха', 'Без добавок': 'КИПЯТОК'}

class Soup:
    def show_my_soup(self, ingridient):
        print(f'Ваш суп - {ingridients[ingridient]}')


for prod in ingridients.keys():
    print(prod)
while True:
    choice = input('Выберите ингридиент: ').capitalize()
    temp = []
    for prod in ingridients.keys():
        temp.append(prod)
    res = choice in temp
    if res == False:
        print('Введите верный ингридиент')
    else:
        break
my_soup = Soup()
my_soup.show_my_soup(choice)