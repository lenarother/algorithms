from copy import deepcopy
import random
import time


def bubble_sort(input_list):
    modified = True
    while modified is True:
        modified = False
        for x in range(len(input_list) - 1):
            if input_list[x] > input_list[x + 1]:
                input_list[x], input_list[x + 1] = input_list[x + 1], input_list[x]
                modified = True
    return input_list


def test_sort_function(sort_function):
    assert sort_function([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert sort_function([6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6]
    assert sort_function([4, 5, 1, 6, 3, 2]) == [1, 2, 3, 4, 5, 6]
    print('OK')


def time_sort_function(sort_function, input_list):
    start = time.time()
    sort_function(input_list)
    end = time.time()
    print(f'{sort_function.__name__}: {end - start}')


if __name__ == '__main__':
    test_sort_function(bubble_sort)
    test_sort_function(bubble_sort_2)
    input_list = list(random.sample(range(10000), 10000))
    time_sort_function(bubble_sort, deepcopy(input_list))
    time_sort_function(sorted, deepcopy(input_list))
