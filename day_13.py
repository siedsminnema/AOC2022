from typing import List

from input import get_input
from collections import Counter

input = get_input(13)


def check_ints(value1: int, value2: int):
    if value2 < value1:
        return 'False'
    if value2 == value1:
        return 'Same'
    else:
        return 'True'


def check_lists(list1, list2):
    # length comparison

    maximal_i = max(len(list1), len(list2))

    for i in range(maximal_i):

        try:
            left = list1[i]
        except:
            return True
        try:
            right = list2[i]
        except:
            return False

        if isinstance(left, int) and isinstance(right, list):
            left = [left]

        if isinstance(right, int) and isinstance(left, list):
            right = [right]

        if isinstance(left, int) and isinstance(right, int):

            int_level = check_ints(left, right)
            if int_level == 'False':
                return False
            if int_level == 'True':
                return True

        if isinstance(left, list) and isinstance(right, list):

            list_level = check_lists(left, right)
            if not list_level:
                return False

        return True

    return 'Not Sure'


# main
total = 0


def check_pair(left, right):
    truthful = 'Not Sure'

    if isinstance(left, int) and isinstance(right, list):
        left = [left]

    if isinstance(right, int) and isinstance(left, list):
        right = [right]

    if isinstance(left, int) and isinstance(right, int):
        int_level = check_ints(left, right)
        if int_level == 'False':
            return False
        if int_level == 'True':
            return True

    if truthful != True:
        if isinstance(left, list) and isinstance(right, list):
            if not check_lists(left, right):
                return False

    return True


for i in range(0, len(input), 3):

    left = eval(input[i])
    right = eval(input[i + 1])

    print(left, right, check_pair(left, right), i, i/3, total, "\n\n\n")

print(total)


