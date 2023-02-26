#!/usr/bin/python3

# this program "rLuv" will receive two args (your name and your crush's) and will output the percentage of  your love's chance to work out

#import sys to get argv listt
import sys
from sys import argv

argc = len(argv)
only_num = False

def process_options(opt):
    match(opt):
        case "help":
            help_msg = f"""usage: {argv[0]} [option] [NAME1 NAME2]
NAME1 | NAME2 is the name of the two memhers of a couple

option can be:
    --help: prints this message
    --version: prints veersion
    --usage: prints a dimple example of using this program
    --onlynum: prints only thr number of percentage

This program will receive 2 names (your name and your crush's)
and output the percentage of chance for your love to work out"""
            print(help_msg)
            return 0

        case "usage":
            print(f"usage: {argv[0]} NAME1 NAME2")
            return 0

        case "version":
            print("rLuv: 1.0")
            return 0

        case "onlynum":
            global only_num, argc
            argc -= 1
            only_num = True
            argv.pop(argv.index("--onlynum"))
            return -1

        case _:
            print("unknown option:", opt)
            return 1


print_usage = False

if argc > 4 and argv[1][2:] != "onlynum":
        print_usage = True

elif argc < 2:
    print_usage = True

elif argv[1][0:2] == "--":
    exit_status = process_options(argv[1][2:])
    if exit_status != -1:
        sys.exit(exit_status)

    else:
        if argc != 3:
            print_usage = True

elif argc != 3:
    print_usage = True

if print_usage:
    sys.exit(process_options("usage"))

def get_pat_array(arr):
    n = len(arr)
    pat = []
    for i in range(n//2):
        pat.append(arr[i] + arr[n-1-i])
    if n % 2 != 0:
        pat.append(arr[n//2])
    return pat


def rlove(name1:str, name2:str) -> int:
    name1 = name1.upper()
    name2 = name2.upper()

    added_letters = []
    numbers = []

    for i in name1 + name2:
        index2letter = 0
        if not i in added_letters:
            added_letters.append(i)
            numbers.append(0)

        index2letter = added_letters.index(i)
        numbers[index2letter] += 1


    while len(numbers) > 2:
        numbers = get_pat_array(numbers)

    return int("".join(map(str, numbers)))


name1 = argv[1]
name2 = argv[2]

percentage = rlove(name1, name2)

print(percentage if only_num else f"the change for {name1} and {name2}'s love work out is {percentage}")
