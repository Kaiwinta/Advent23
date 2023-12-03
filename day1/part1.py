##
## EPITECH PROJECT, 2023
## Advent23-01
## File description:
## day1.py
##

f = open("day1/test.txt", "r")

def line_check(fd, char):
    nb_1 = 0
    nb_2 = 0
    counter = 0
    while (char != '\n'):
        try:
            int(char)
            if counter == 0:
                nb_1 = int(char)
                nb_2 = int(char)
                counter += 1
            else:
                nb_2 = int(char)
                counter +=1
        except:
            pass
        char = fd.read(1)
    return nb_1 * 10 + nb_2


def line_loop(fd):
    char = fd.read(1)
    nb = 0
    while char:
        nb += (line_check(fd, char))
        char = fd.read(1)
    print(nb)

line_loop(f)