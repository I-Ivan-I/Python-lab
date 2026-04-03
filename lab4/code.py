from functools import lru_cache

# Задание 1: Линеаризация
def linearize_iter(lst):
    result, stack = [], lst[::-1]
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item[::-1])
        else:
            result.append(item)
    return result

def linearize_rec(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(linearize_rec(item))
        else:
            result.append(item)
    return result

# Задание 2: Последовательность
def calc_ab_iter(k):
    if k < 1: return None
    a = b = 1
    for _ in range(2, k + 1):
        a, b = 2*b + a, 2*a + b
    return a, b

@lru_cache(maxsize=None)
def calc_ab_rec(k):
    if k == 1: return (1, 1)
    a_prev, b_prev = calc_ab_rec(k - 1)
    return (2*b_prev + a_prev, 2*a_prev + b_prev)

# Вывод результатов 
if __name__ == "__main__":
    test_list = [1, 2, [3, 4, [5, [6, []]]]]
    print(f"  Итеративно: {linearize_iter(test_list)}")
    print(f"  Рекурсивно: {linearize_rec(test_list)}")
    
    print('')
    for k in range(1, 8):
        iter_res = calc_ab_iter(k)
        rec_res = calc_ab_rec(k)
        print(f"  k={k}: iter={iter_res}, rec={rec_res}")
