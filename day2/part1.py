##
## EPITECH PROJECT, 2023
## Advent23-01
## File description:
## day1.py
##

f = open("day2/day2_input.txt", "r")

def check_game(last, end, char):
    u = last
    nb = 0

    while char[u] != ' ':
        nb  = nb * 10
        nb += int(char[u])
        u += 1
    # print("nb = " + str(nb))
    u += 1
    if char[u : u + 4] =="blue":
        u = u + 4
        # print("blue = " + str(nb))
        if nb > 14:
            return -1
    if char[u : u + 3] == 'red':
        u = u + 3
        # print("red = " + str(nb))
        if nb > 12:
            return -1
    if char[u : u + 5] == "green":
        # print("green = " + str(nb))
        u = u + 5
        if nb > 13:
            return -1
    if u + 2 < end:
        return check_game(u + 2, end, char)
    return 1

def cut_game(i, char):
    last = i
    for t in range(i, len(char)):
        if char[t] == ';' or char[t] == '\n':
            # print(char[last:t])
            nb = check_game(last, t, char)
            if nb == -1:
                return -1
            last = t + 2
    return 1

def cut_line(char):
    u = 5
    id = 0
    while char[u] != ':':
        id  = id * 10
        id += int(char[u])
        u += 1
    print(id)
    for i in range(len(char)):
        if char[i] == ":":
            y = i + 2
    if cut_game(y, char) == 1:
        return int(id)
    else:
        # print(str(id))
        return 0

def line_loop2(fd):
    char = fd.readline()
    nb = 0
    while char:
        nb += cut_line(char)
        char = fd.readline()
    print(nb)

line_loop2(f)