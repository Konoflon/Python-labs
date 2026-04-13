import itertools
from functools import lru_cache


def split_iter_opt(lst, n):
    return [lst[i::n] for i in range(n)]


def split_rec_opt(lst, n, i=0, result=None):
    if result is None:
        result = [lst[i::n] for i in range(n)]
        return result
    if i >= len(lst):
        return result
    result[i % n].append(lst[i])
    return split_rec_opt(lst, n, i + 1, result)


@lru_cache(maxsize=None)
def calc_v_rec_opt(i):
    if i == 1 or i == 2:
        return 0
    if i == 3:
        return 1.5
    return (i + 1) / (i * i + 1) * calc_v_rec_opt(i - 1) - calc_v_rec_opt(i - 2) * calc_v_rec_opt(i - 3)


def calc_v_iter_opt(i):
    if i < 3:
        return 0
    if i == 3:
        return 1.5
    v1, v2, v3 = 0.0, 0.0, 1.5
    for k in range(4, i + 1):
        v_new = (k + 1) / (k * k + 1) * v3 - v2 * v1
        v1, v2, v3 = v2, v3, v_new
    return v3


print(split_iter_opt([1, 2, 3, 4, 5], 2))
print(split_rec_opt([1, 2, 3, 4, 5], 2))
print(split_iter_opt([1, 2, 3, 4, 5], 3))
print(split_rec_opt([1, 2, 3, 4, 5], 3))

for i in range(1, 11):
    print(calc_v_iter_opt(i))