# Simple examples of binary search

import time


def binary_search(lst, item):
    start_time = time.time()
    low = 0
    high = len(lst) - 1
    counter = 1
    while low <= high:
        mid = (high + low) // 2
        guess = lst[mid]
        if guess == item:
            return f'{mid: _} element', f'time {time.time() - start_time}', f'{counter: _} - steps'
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
        counter += 1
    return None

def usual_alg(lst, item):
    start_time = time.time()
    counter = 1
    for i in range(len(lst)):
        if my_list_1[i] == item:
            return f'{i: _} element', f'time {time.time() - start_time}', f'{counter: _} - steps'
        counter += 1
    return None


my_list_1 = list(range(20)) + list(range(30, 600_000))
item = 552_424

print(binary_search(my_list_1, item), end= '\n'*2)
print(usual_alg(my_list_1, item), end= '\n'*2)
