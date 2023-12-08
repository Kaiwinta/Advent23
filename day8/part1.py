##
## EPITECH PROJECT, 2023
## Advent23-01
## File description:
## part1.py
##

import cProfile

f = open("day8/day8_input.txt", "r")

def search_next(list_dico, to_find, dico):
    return list_dico[dico[to_find]]

def execute_instruction(list_dico, intructions, dico):
    len_instruction = len(intructions)
    actual = list_dico[0]
    nb_step = 0
    end_conditions = {'ZZZ'}
    while actual[0] not in end_conditions:
        actual = search_next(list_dico, actual[1][intructions[nb_step % len_instruction] == 'R'], dico)
        nb_step += 1
    print(nb_step)

def change_in_dico(list_input):
    dico = {}
    for i in range(len(list_input)):
        dico[str(list_input[i][0])] = i
    return dico

def analyse_line(actual):
    temp = [actual[0:3], [actual[7: 10], actual[12: 15]]]
    return temp

def main(f):
    instructions = f.readline()[:-1] #Get the instruction line
    f.readline()    #skip the blank line
    list_input = []
    actual = f.readline()
    while actual:
        list_input.append(analyse_line(actual[:-1]))
        actual =  f.readline()
    dico = change_in_dico(list_input)
    execute_instruction(list_input, instructions, dico)

if __name__ == "__main__":
    main(f)