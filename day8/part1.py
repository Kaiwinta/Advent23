##
## EPITECH PROJECT, 2023
## Advent23-01
## File description:
## part1.py
##

import cProfile

f = open("day8/day8_input.txt", "r")

def execute_instruction(intructions, dico):
    len_instruction = len(intructions)
    actual = dico[[*dico][0]]
    nb_step = 0
    end_conditions = {'ZZZ'}
    while actual[0] not in end_conditions:
        actual = dico[actual[1][intructions[nb_step % len_instruction] == 'R']]
        nb_step += 1
    print(nb_step)

def change_in_dico(list_input):
    dico = {str(item[0]): [item[0], item[1]] for item in list_input}
    return dico

def analyse_line(actual):
    temp = [actual[0:3], [actual[7: 10], actual[12: 15]]]
    return temp

def main(f):
    instructions = f.readline()[:-1] #Get the instruction line
    f.readline()    #skip the blank line
    list_input = [analyse_line(line[:-1]) for line in f]
    dico = change_in_dico(list_input)
    execute_instruction(instructions, dico)

if __name__ == "__main__":
    main(f)