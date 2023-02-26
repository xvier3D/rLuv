# imports sys module and argv from sys module to be changeable
import sys
from sys import argv

if argv[0] == ".":
    argv[0] = "rLuv"

argc = len(argv)

# public functions of tgis module
__ALL__ = ["process_options", "get_pat_array", "rlove"]

def process_options(opt:str) -> int:
    """
    this function will receive an option string
    and process it to do the expected thing
    opt: of type str is an option to use
    """
    # match statement to use like switch(opt){ case: "main"  break; }
    match(opt):
        case "help":
            # in case option being help it will print an helpful message 
            help_msg = f"""usage: {argv[0]} [option] [NAME1 NAME2]
NAME1 | NAME2 is the name of the two memhers of a couple

option can be:
    --help: prints this message
    --version: prints version
    --usage: prints a simple example of using this program
    --onlynum: prints only thr number of percentage

This program will receive 2 names (your name and your crush's)
and output the percentage of chance for your love to work out"""
            # prints help message
            print(help_msg)
            # returns 0 to indicate that the program has to exit with 0 status code
            return 0

        case "usage":
            # in case of option being `--usage` it will print a simple example of how to use this python program
            print(f"usage: {argv[0]} NAME1 NAME2")
            return 0

        case "version":
            # in case --version it will print  the name of the program and the version  being that 1.0
            print("rLuv: 1.0")
            return 0

        case "onlynum":
            # onlynum option will set only_num to True causing the output of the program print only the number of percentage
            # adds globals variable to change itt
            global only_num, argc
            # since it will pop the arg `--onlynum` from  it will decrease the argc by 1
            argc -= 1
            only_num = True
            argv.pop(argv.index("--onlynum"))
            # returning -1 will indicatethat program doesn't need to stop
            return -1

        case _:
            # default means unknown option
            print("unknown option:", opt)
            # returns 1 meaning error
            return 1


def get_pat_array(arr):
    """
    receives an input array and returns a
    PAT (Pairwise Addition Transformed) array of
    the input
    arr: an input array to be transformed
    """
    n = len(arr)
    pat = []
    for i in range(n//2):
        pat.append(arr[i] + arr[n-1-i])
    if n % 2 != 0:
        pat.append(arr[n//2])
    return pat


def rlove(name1:str, name2:str) -> int:
    """
    receives two names and returns the
    percentage of chance for the love's work out
    name1 | name2: names of people of the couple
    """
    # uppers the name for not having confusion of letter A and a
    name1 = name1.upper()
    name2 = name2.upper()

    # creates 2 arrays one for not adding alrady added letter again other to be the array of numbers to get the PAT one
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

    # return the int value of an int like  list([4, 7]) == int(47)
    return int("".join(map(str, numbers)))


