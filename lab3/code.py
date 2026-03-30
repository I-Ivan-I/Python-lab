import itertools

def task1_vasya_words():
    alphabet = ['К', 'А', 'Т', 'Е', 'Р']
    count = 0
    for p in itertools.product(alphabet, repeat=6):
        if p[0] == 'Р' and p[-1] == 'К':
            count += 1
    return count

def task2_count_ones():
    val = (216**6) + (216**4) + (36**6) - (6**14) - 24
    if val == 0: return 1
    digits = []
    while val > 0:
        digits.append(str(val % 6))
        val //= 6
    return len(set(digits))

def task3_find_numbers():
    results = []
    for d1 in range(10):
        for d2 in range(10):
            num = int(f"12345{d1}7{d2}8")
            if num <= 10**9 and num % 23 == 0:
                results.append((num, num // 23))
    return sorted(results)

# Вывод результатов
print(f"Ответ: {task1_vasya_words()} слов")
print(f"Ответ: {task2_count_ones()} различных цифр")

ans3 = task3_find_numbers()
print(f"Найдено чисел: {len(ans3)}")
for num, div in ans3:
    print(num, div)