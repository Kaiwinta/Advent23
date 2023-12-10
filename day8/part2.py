##
## EPITECH PROJECT, 2023
## Advent23-01
## File description:
## part1.py
##

import cProfile

f = open("day8/day8_input.txt", "r")

def check_ended(list_actual):
    return not any(i[0][-1] != "Z" for i in list_actual)

def move_actual(list_actual, dico, nb_step, len_instruction, intructions):
    return [dico[item[1][intructions[nb_step % len_instruction] == 'R']] for item in list_actual]

def execute_instruction(intructions, dico, list_actual):
    len_instruction = len(intructions)
    nb_step = 0
    ended = 0
    while ended == 0:
        list_actual = move_actual(list_actual, dico, nb_step, len_instruction, intructions)
        ended = check_ended(list_actual)
        nb_step += 1
    print(nb_step)

def change_in_dico(list_input):
    return {str(item[0]): [item[0], item[1]] for item in list_input}

def analyse_line(actual):
    return [actual[0:3], [actual[7: 10], actual[12: 15]]]

def search_start(list_input):
    return [item for item in list_input if item[0][-1] =='A']

def main(f):
    instructions = f.readline()[:-1] #Get the instruction line
    f.readline()    #skip the blank line
    list_input = [analyse_line(line[:-1]) for line in f]
    start = search_start(list_input)
    dico = change_in_dico(list_input)
    print(dico)
    print(start)
    execute_instruction(instructions, dico, start)

if __name__ == "__main__":
    main(f)