from copy import deepcopy
import random

from base import test_sort_function, time_sort_function


def selection_sort(input_list):
    for x in range(len(input_list) - 1):
        min_pos = x
        for y in range(x + 1, len(input_list)):
            if input_list[y] < input_list[min_pos]:
                min_pos = y
        input_list[x], input_list[min_pos] = input_list[min_pos], input_list[x]

    return input_list


if __name__ == '__main__':
    test_sort_function(selection_sort)

    input_list = list(random.sample(range(10000), 10000))
    time_sort_function(selection_sort, deepcopy(input_list))
    time_sort_function(sorted, deepcopy(input_list))
