import os

file_name = "day3/day3_input.txt"

def analyse_array(array):
    nb = 0
    for i in range(len(array)):
        for y in range(len(array[i])):
            u = 0
            if array[i][y] != '.':
                while(u != -1 and array[i][y]):
                    try:
                        print(array[i][y])
                        nb = int(array[i][y : y + u])
                        u += 1
                    except:
                        # print(nb)
                        # print(array[i][y])
                        u = -1

def main(file_name):
    txt_file = open(file_name)

    count = 0

    array  = []
    for line in txt_file:
        array.append(line[0 : -1])
    count += 1

    txt_file.close()
    analyse_array(array)
    print(array)

if __name__ =="__main__":
    main(file_name)