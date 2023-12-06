##
## EPITECH PROJECT, 2023
## Advent23-01
## File description:
## part1.py
##

def round(distance, time):
    try_distance = 0
    total_ways = 0

    for holding in range(time):
        try_distance = holding * (time - holding)
        if try_distance > distance:
            total_ways += 1
    return total_ways


def main():
    list_time1 = [53,83,72,88]
    list_distance1 = [333,1635,1289,1532]
    total1 = 1

    for i in range(len(list_distance1)):
        total1 *= (round(list_distance1[i], list_time1[i]))
    print(total1)
    list_time2 = [53837288]
    list_distance2 = [333163512891532]
    total2 = 1

    for i in range(len(list_distance2)):
        total2 *= (round(list_distance2[i], list_time2[i]))
    print(total2)

if __name__ == "__main__":
    main()