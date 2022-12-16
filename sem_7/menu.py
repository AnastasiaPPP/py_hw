import actions
import export as ex


def start_menu():
    while True:
        inp = int(input('***МЕНЮ*** \n Выберите действие: \n 1. Добавить событие в календарь \n 2. Показать календарь \n 3. Экспорт \n 4. Выход из меню '))
        if inp == 4:
            break
        elif inp == 1:
            days = {1: 'Понедельник', 2: 'Вторник', 3: 'Среда', 4: 'Четверг', 5: 'Пятница', 6: 'Суббота', 7: 'Воскресенье'}
            for key, value in days.items():
                print(key, ':', ''.join(str(x) for x in value))
            day = days[int(input('Выберите день недели: '))]
            tm = input('Запишите время события: ')
            wr = input('Событие: ')
            actions.write_event(day, tm, wr)
        elif inp == 2:
            actions.show_calendar()
        else:
            extension = ''
            type = int(input('Укажите расширене для экспорта: \n 1. json 2. scv 3. html 4. yml '))
            if type == 1:
                extension = 'json'
            elif type == 2:
                extension = 'scv'
            elif type == 3:
                extension = 'html'
            else:
                extension = 'yml'
            ex.export(extension)