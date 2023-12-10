##
## EPITECH PROJECT, 2023
## Advent23-01
## File description:
## part1.py
##

f = open("day9/day9_input.txt", "r")

def test_on_line(line):
    underline = []
    for i in range(1, len(line)):
        underline.append(line[i] - line[i - 1])
    if not all(item == 0 for item in underline):
        underline.append(underline[-1] + test_on_line(underline))
        return underline[-1]
    return 0

def main(f):
    list_input = [list(map(int, line.split())) for line in f]
    nb = 0
    for i in list_input:
        nb += i[-1] + test_on_line(i)
    print(nb)

if __name__ == "__main__":
    main(f)