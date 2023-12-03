##
## EPITECH PROJECT, 2023
## Advent23-01
## File description:
## day1.py
##

class input:
    def __init__(self):
        self.red = 0
        self.green = 0
        self.blue = 0

f = open("day2/day2_input.txt", "r")

def check_game(last, end, char, input):
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
        if nb > input.blue:
            input.blue = nb
    if char[u : u + 3] == 'red':
        u = u + 3
        # print("red = " + str(nb))
        if nb > input.red:
            input.red = nb
    if char[u : u + 5] == "green":
        u = u + 5
        if nb > input.green:
            input.green = nb
    if u + 2 < end:
        return check_game(u + 2, end, char, input)
    return 1

def cut_game(i, char):
    last = i
    nb = 0
    game = input()
    for t in range(i, len(char)):
        if char[t] == ';' or char[t] == '\n':
            check_game(last, t, char, game)
            last = t + 2
    nb = game.red * game.green * game.blue
    return nb

def cut_line(char):
    u = 5
    nb = 0
    for i in range(len(char)):
        if char[i] == ":":
            y = i + 2
    nb += cut_game(y, char)
    return nb

def line_loop2(fd):
    char = fd.readline()
    nb = 0
    while char:
        nb += cut_line(char)
        char = fd.readline()
    print(nb)

line_loop2(f)