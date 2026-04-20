def split_iter(lst, n):
    result = [[] for _ in range(n)]
    for i, item in enumerate(lst):
        result[i % n].append(item)
    return result

def split_rec(lst, n, i=0, result=None):
    if result is None:
        result = [[] for _ in range(n)]
    if i >= len(lst):
        return result
    result[i % n].append(lst[i])
    return split_rec(lst, n, i + 1, result)

def calc_v_iter(i):
    if i <= 2:
        return 0
    if i == 3:
        return 1.5
    v1, v2, v3 = 0, 0, 1.5
    for k in range(4, i + 1):
        v_new = (k + 1) / (k * k + 1) * v3 - v2 * v1
        v1, v2, v3 = v2, v3, v_new
    return v3

cache = {}

def calc_v_rec(i):
    if i in cache:
        return cache[i]
    if i <= 2:
        return 0
    if i == 3:
        return 1.5
    result = (i + 1) / (i * i + 1) * calc_v_rec(i - 1) - calc_v_rec(i - 2) * calc_v_rec(i - 3)
    cache[i] = result
    return result

def run():
    print("Lab4: split_iter([1,2,3,4,5], 2) =", split_iter([1,2,3,4,5], 2))
    print("Lab4: split_rec([1,2,3,4,5], 2) =", split_rec([1,2,3,4,5], 2))
    print("Lab4: V(1..5) =", [calc_v_iter(i) for i in range(1, 6)])