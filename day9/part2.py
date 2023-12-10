##
## EPITECH PROJECT, 2023
## Advent23-01
## File description:
## part1.py
##

f = open("day9/day9_input.txt", "r")

def test_on_line(line):
    underline = []
    for i in range(0, len(line) - 1):
        underline.append(line[i + 1] - line[i])
    if not all(item == 0 for item in underline):
        underline.insert(0, underline[0] - test_on_line(underline))
        return underline[0]
    underline.insert(0, 0)
    return underline[0]

def main(f):
    list_input = [list(map(int, line.split())) for line in f]
    nb = 0
    for i in list_input:
        nb += i[0] - test_on_line(i)
    print(nb)

if __name__ == "__main__":
    main(f)