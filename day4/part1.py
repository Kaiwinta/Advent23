##
## EPITECH PROJECT, 2023
## Advent23-01
## File description:
## day1.py
##

f = open("day4/day4_input.txt", "r")

def cut_line(char):
    number_list ="1234567890"
    nb_list = []
    for i in range(len(char)):
        if char[i] == ":":
            y = i + 2
    nb = -1
    while char[y] != '|':
        if char[y] in number_list:
            if nb == -1:
                nb = 0
            nb *= 10
            nb += int(char[y])
        if char[y] == " ":
            if (nb) != -1:
                nb_list.append(nb)
            nb = -1
        y += 1
    nb = -1
    y += 1
    total = 0
    while char[y] != '\n':
        if char[y] in number_list:
            if nb == -1:
                nb = 0
            nb *= 10
            nb += int(char[y])
        if char[y] == " ":
            if (nb) != -1:
                if nb in nb_list:
                    if total == 0:
                        total = 1
                    else:
                        total *= 2

            nb = -1
        y += 1
    if (nb) != -1:
                if nb in nb_list:
                    if total == 0:
                        total = 1
                    else:
                        total *= 2
    return total

def line_loop2(fd):
    char = fd.readline()
    total = 0
    while char:
        total += cut_line(char)
        char = fd.readline()
    print(total)

line_loop2(f)