def split_iter(lst, n):
    result = []
    for i in range(n):
        result.append([])
    for i in range(len(lst)):
        result[i % n].append(lst[i])
    return result

def split_rec(lst, n, i=0, result=None):
    if result is None:
        result = []
        for j in range(n):
            result.append([])
    if i >= len(lst):
        return result
    result[i % n].append(lst[i])
    return split_rec(lst, n, i + 1, result)

def calc_v_iter(i):
    if i == 1 or i == 2:
        return 0
    if i == 3:
        return 1.5
    v1 = 0
    v2 = 0
    v3 = 1.5
    for k in range(4, i + 1):
        v_new = (k + 1) / (k * k + 1) * v3 - v2 * v1
        v1 = v2
        v2 = v3
        v3 = v_new
    return v3

cache = {}

def calc_v_rec(i):
    if i in cache:
        return cache[i]
    if i == 1 or i == 2:
        return 0
    if i == 3:
        return 1.5
    result = (i + 1) / (i * i + 1) * calc_v_rec(i - 1) - calc_v_rec(i - 2) * calc_v_rec(i - 3)
    cache[i] = result
    return result

print(split_iter([1,2,3,4,5], 2))
print(split_rec([1,2,3,4,5], 2))
print(split_iter([1,2,3,4,5], 3))
print(split_rec([1,2,3,4,5], 3))

for i in range(1, 11):
    print(calc_v_iter(i))