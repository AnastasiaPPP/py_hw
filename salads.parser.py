import requests
from bs4 import BeautifulSoup as bs
import os
os.system('cls||clear') 


url = 'https://www.russianfood.com/recipes/bytype/?fid=35' #рецепты салатов 
page = requests.get(url)
soup = bs(page.text, 'html.parser')
ingridient = soup.find_all('div', class_='ingr_str')

def list_of_ingridients(ingr): #список ингридиентов салатов 
    recipes = []
    for res in ingr:
        r = [res.text]
        recipes.append(r)
    return recipes
list_of_ingridients(ingridient)

name = soup.find_all('div', class_='title_o')

def list_of_salad_names(n):  #список названий салатов
    headers = []
    for name in n:
        head = [name.text]
        headers.append(head)
    return headers


def print_strings(lst_of_strgs):
        for item in lst_of_strgs:
            for p in item:
                print(p, end=' ')

salads = list_of_salad_names(name)
ingrs = list_of_ingridients(ingridient)
#print_strings(ingrs)
# print()                 показывает списки ингридиентов и списки названий салатов
# print_strings(salads)

t_of_ingrs = ('сыр твёрдый', 'помидоры', 'яйца', 'рис', 'шампиньоны', 'крабовые палочки', 'ветчина', 'кукуруза', 'куриная грудка', 'морковь', 'огурцы маринованные', 'капуста пекинская', 'огурцы свежие', 'картофель')
print('Список ингридиентов: \n')
for val, i in enumerate(t_of_ingrs, 0):
    print(val, i)

user_choice = list(map(int, input('Введите номер ингридиента(-ов): \n').split()))
print('Салаты в которых присутсвуют такие ингридиенты: \n')
choice_list = [t_of_ingrs[x] for x in user_choice]

for item in ingrs:
    for ch in choice_list:
        if str(ch) in str(item):
            ind = ingrs.index(list(item))
            print(', '.join(salads[ind]))

