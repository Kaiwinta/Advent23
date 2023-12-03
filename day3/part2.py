import os

file_name = "day3/day3_input.txt"

class input:
    def __init__(self):
        self.listx = []
        self.listy = []
        self.listnearing = []
    
def check_next(array, i, y, symbol):
    no_list = "12345467890."
    try:
        if array[i - 1][y] not in no_list:
            for t in range(len(symbol.listx)):
                if symbol.listy[t] == i - 1 and symbol.listx[t] == y:
                    return t
    except:
        pass
    try:
        if array[i + 1][y] not in no_list:
            for t in range(len(symbol.listx)):
                if symbol.listy[t] == i + 1 and symbol.listx[t] == y:
                    return t
    except:
        pass
    try:
        if array[i][y + 1] not in no_list:
            for t in range(len(symbol.listx)):
                if symbol.listy[t] == i and symbol.listx[t] == y + 1:
                    return t
    except:
        pass
    try:
        if array[i][y - 1] not in no_list:
            for t in range(len(symbol.listx)):
                if symbol.listy[t] == i and symbol.listx[t] == y - 1:
                    return t
    except:
        pass
    try:
        if array[i + 1][y + 1] not in no_list:
            for t in range(len(symbol.listx)):
                if symbol.listy[t] == i + 1 and symbol.listx[t] == y + 1:
                    return t
    except:
        pass
    try:
        if array[i - 1][y + 1] not in no_list:
            for t in range(len(symbol.listx)):
                if symbol.listy[t] == i - 1 and symbol.listx[t] == y + 1:
                    return t
    except:
        pass
    try:
        if array[i - 1][y - 1] not in no_list:
            for t in range(len(symbol.listx)):
                if symbol.listy[t] == i - 1 and symbol.listx[t] == y - 1:
                    return t
    except:
        pass
    try:
        if array[i + 1][y - 1] not in no_list:
            for t in range(len(symbol.listx)):
                if symbol.listy[t] == i + 1 and symbol.listx[t] == y - 1:
                    return t
    except:
        pass
    return -1

def calcul_end(symbol):
    sum = 0
    for id in range(len(symbol.listx)):
        if symbol.listnearing[id][0] != -1 and symbol.listnearing[id][1] != -1:
            sum += symbol.listnearing[id][0] * symbol.listnearing[id][1]
    print(sum)
    return sum

def check_number(array, symbol):
    number_list = "12345467890"
    print(symbol.listx)
    print(symbol.listy)
    for y in range(len(array)):
        x = 0
        while x < len(array[y]):
            u = 0
            nb = 0
            nearing = []
            while x + u < len(array[y]) and array[y][x + u] in number_list:
                nearing .append(check_next(array, y, x + u, symbol))
                nb  = nb * 10
                nb += int(array[y][x + u])
                u += 1
            if nb > 0:
                nearing = set(nearing)
                for w in nearing:
                    if w != -1:
                        if symbol.listnearing[w][0] == -1:
                            symbol.listnearing[w][0] = nb
                        else:
                            symbol.listnearing[w][1] = nb
            x += u + 1
    return calcul_end(symbol)

def analyse_array(array):
    no_list = "12345467890."
    symbol = input()
    sum = 0
    for y in range(len(array)):
        x = 0
        while x < len(array[y]):
            if array[y][x] not in no_list:
                print(array[y][x])
                symbol.listx.append(x)
                symbol.listy.append(y)
                symbol.listnearing.append([-1, -1])
            x += 1
    check_number(array, symbol)

def main(file_name):
    txt_file = open(file_name)

    count = 0

    array  = []
    for line in txt_file:
        array.append(line[0 : -1])
    count += 1

    txt_file.close()
    analyse_array(array)

if __name__ =="__main__":
    main(file_name)