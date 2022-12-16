file = 'calendar.txt'


def write_event(day, time, event):
    with open(file, 'a', encoding='utf-8') as f:
        f.write('\n {} {} - {}'.format(day, time, event))

def show_calendar():
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            print(line)







