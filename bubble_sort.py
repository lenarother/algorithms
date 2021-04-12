from copy import deepcopy
import random

from base import test_sort_function, time_sort_function


def bubble_sort(input_list):
    modified = True
    while modified is True:
        modified = False
        for x in range(len(input_list) - 1):
            if input_list[x] > input_list[x + 1]:
                input_list[x], input_list[x + 1] = input_list[x + 1], input_list[x]
                modified = True
    return input_list


if __name__ == '__main__':
    test_sort_function(bubble_sort)
    input_list = list(random.sample(range(10000), 10000))
    time_sort_function(bubble_sort, deepcopy(input_list))
    time_sort_function(sorted, deepcopy(input_list))
