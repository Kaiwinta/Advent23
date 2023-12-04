##
## EPITECH PROJECT, 2023
## Advent23-01
## File description:
## day1.py
##

f = open("day4/day4_input.txt", "r")

class game:
    def __init__(self):
        self.list_game = []
    
    def adding_size(self, size):
        for i in range(size):
            self.list_game.append([i, 1])
        
    def getsum(self):
        total = 0
        for i in range(len(self.list_game)):
            total += self.list_game[i][1]
        return total

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
                    total += 1

            nb = -1
        y += 1
    if (nb) != -1:
                if nb in nb_list:
                    total+=1
    return total

def line_loop2(fd):
    stat = game()
    char = fd.readline()
    total = 0
    stat.adding_size(190)
    line = 0
    while char:
        actual = cut_line(char)
        for y in range(stat.list_game[line][1]):
            for i in range(actual):
                if i + line + 1 < 190:
                    stat.list_game[i + line + 1][1] += 1
        char = fd.readline()
        line += 1
    print(stat.getsum())

line_loop2(f)