#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # Siyahının kopyasını tərsinə çevirib üzərində dövr edirik
    for i in my_list[::-1]:
        print("{:d}".format(i))
