import os

file_name = "day3/day3_input.txt"

def check_next(array, i, y):
    no_list = "12345467890."
    try:
        if array[i - 1][y] not in no_list:
            return 1
    except:
        pass
    try:
        if array[i + 1][y] not in no_list:
            return 1
    except:
        pass
    try:
        if array[i][y + 1] not in no_list:
            return 1
    except:
        pass
    try:
        if array[i][y - 1] not in no_list:
            return 1
    except:
        pass
    try:
        if array[i + 1][y + 1] not in no_list:
            return 1
    except:
        pass
    try:
        if array[i - 1][y + 1] not in no_list:
            return 1
    except:
        pass
    try:
        if array[i - 1][y - 1] not in no_list:
            return 1
    except:
        pass
    try:
        if array[i + 1][y - 1] not in no_list:
            return 1
    except:
        pass
    return 0

def analyse_array(array):
    number_list = "12345467890"
    sum = 0
    for i in range(len(array)):
        w = 0
        while w < len(array[i]):
            u = 0
            nb = 0
            nearing = 0
            while w + u < len(array[i]) and array[i][w + u] in number_list:
                nearing += check_next(array, i, w + u)
                nb  = nb * 10
                nb += int(array[i][w + u])
                u += 1
            w += u
            if nearing > 0:
                print(nb)
                sum += nb
            w += 1
    print(sum)
    

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