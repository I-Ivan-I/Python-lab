from functools import lru_cache

def linearize_iter(lst):
    result = []
    stack = lst[::-1]
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

def calc_ab_iter(k):
    if k < 1:
        return None
    a = 1
    b = 1
    for _ in range(2, k + 1):
        a, b = 2 * b + a, 2 * a + b
    return a, b

@lru_cache(maxsize=None)
def calc_ab_rec(k):
    if k == 1:
        return (1, 1)
    a_prev, b_prev = calc_ab_rec(k - 1)
    return (2 * b_prev + a_prev, 2 * a_prev + b_prev)