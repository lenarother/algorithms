import time


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
