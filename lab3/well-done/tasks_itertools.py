import itertools

class WordCounter:
    def __init__(self, alphabet, length):
        self.alphabet = alphabet
        self.length = length

    def solve(self, conditions):
        count = 0
        for word in itertools.product(self.alphabet, repeat=self.length):
            if all(cond(word) for cond in conditions):
                count += 1
        return count

class BinaryCounter:
    def __init__(self, number):
        self.number = number

    def solve(self):
        return bin(self.number)[2:].count('1')

class NumberFinder:
    def __init__(self, formula, ranges, min_val, max_val):
        self.formula = formula
        self.ranges = ranges
        self.min_val = min_val
        self.max_val = max_val

    def solve(self):
        res = []
        for params in itertools.product(*self.ranges):
            val = self.formula(*params)
            if self.min_val <= val <= self.max_val:
                res.append(val)
        res.sort()
        return res

t1 = WordCounter(['В', 'И', 'Ш', 'Н', 'Я'], 6)
vowels = {'И', 'Я'}
print(f"Ответ: {t1.solve([lambda w: w.count('В') <= 1, lambda w: w[0] != 'Ш', lambda w: w[-1] not in vowels])} слов")

t2 = BinaryCounter(4**2014 + 2**2015 - 8)
print(f"Ответ: {t2.solve()} единиц")

t3 = NumberFinder(lambda m, n: (2 ** m) * (3 ** n), [range(0, 30, 2), range(1, 20, 2)], 400000000, 600000000)
ans = t3.solve()
print(f"Найдено чисел: {len(ans)}")
for num in ans:
    print(num)