def apply_func_n_times(sequence, func, n):
    for item in sequence:
        result = item
        for _ in range(n):
            result = func(result)
        yield result