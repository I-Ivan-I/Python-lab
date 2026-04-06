def apply_func_n_times(sequence, func, n):
    """
    Генератор: применяет func к каждому элементу sequence N раз.
    """
    for item in sequence:
        result = item
        for _ in range(n):
            result = func(result)
        yield result

# Демонстрация работы
if __name__ == "__main__":
    # Пример: возводим 2 в квадрат 3 раза (2 - 4 - 16 - 256)
    data = [2, 3]
    func = lambda x: x ** 2
    n = 3
    
    # Распаковываем генератор в список, чтобы увидеть результат
    print(list(apply_func_n_times(data, func, n)))