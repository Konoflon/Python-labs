import itertools


def task1_vasya_words():
    letters = ['В', 'И', 'Ш', 'Н', 'Я']
    vowels = ['И', 'Я']
    count = 0
    
    for word in itertools.product(letters, repeat=6):
        if word.count('В') > 1:
            continue
        if word[0] == 'Ш':
            continue
        if word[-1] in vowels:
            continue
        count += 1
    
    return count


def task2_count_ones():
    number = 2**4028 + 2**2015 - 2**3
    binary_string = bin(number)[2:]
    ones_count = binary_string.count('1')
    return ones_count


def task3_find_numbers():
    min_value = 400000000
    max_value = 600000000
    result = []
    
    for m in range(0, 30, 2):
        for n in range(1, 20, 2):
            N = (2 ** m) * (3 ** n)
            if N >= min_value and N <= max_value:
                result.append(N)
    
    result.sort()
    return result

answer1 = task1_vasya_words()
print(f"Ответ: {answer1} слов")

answer2 = task2_count_ones()
print(f"Ответ: {answer2} единиц")

answer3 = task3_find_numbers()
print(f"Найдено чисел: {len(answer3)}")
print("Числа в порядке возрастания:")
for number in answer3:
    print(f"  {number}")