##
## EPITECH PROJECT, 2023
## Advent23-01
## File description:
## part1.py
##

f = open("day7/day7_input.txt", "r")

def check_single_hand(card):
    card_list = {}
    for i in card:
        if str(i) not in card_list.keys():
            card_list[str(i)] = 1
        else:
            card_list[str(i)] += 1
    if any(i == 5 for i in card_list.values()):
        return 7
    if any(i == 4 for i in card_list.values()):
        return 6
    if any(i == 3 for i in card_list.values()):
        if any(i == 2 for i in card_list.values()):
            return 5
        return 4
    if sum(value == 2 for value in card_list.values()) > 1:
        return 3
    elif 2 in card_list.values():
        return 2
    return 1

def check_hand(list_input):
    for i in range(len(list_input)):
        list_input[i]["hand"] = check_single_hand(list_input[i]["card"])


def main(f):
    list_input = [list(map(str, line.split())) for line in f]
    list_input = [{"card": item[0], "bet": int(item[1]), "rank": 0, "hand": 0} for item in list_input]
    nb = 0
    check_hand(list_input)
    print(list_input)
    print(nb)

if __name__ == "__main__":
    main(f)