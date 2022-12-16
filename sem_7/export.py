def export(extension):
    with open('calendar.txt', 'r') as data:
        d = data.readlines()
        for line in d:
            with open(f'temp.{extension}', 'w') as file:
                file.write(line)