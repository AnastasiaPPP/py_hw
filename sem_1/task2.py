for x in range(2):
    for y in range(2):
        for z in range(2):
            left = not(x or y or z)
            rigth = not x and not y and not z
            print(left == rigth, end=" ")