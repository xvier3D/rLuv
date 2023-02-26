#!/usr/bin/python3

# this program "rLuv" will receive two args (your name and your crush's) and will output the percentage of  your love's chance to work out

#import sys to get argv listt
import sys

from funcs import process_options, get_pat_array, rlove, argc, argv

only_num = False

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
        argc -= 1
        only_num = True
        if argc != 3:
            print_usage = True

elif argc != 3:
    print_usage = True

if print_usage:
    sys.exit(process_options("usage"))


name1 = argv[1]
name2 = argv[2]

percentage = rlove(name1, name2)

print(percentage if only_num else f"the chance for {name1} and {name2}'s love work out is {percentage}")

