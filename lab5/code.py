import functools

def validate_args(types=None, ranges=None):
    types = types or {}
    ranges = ranges or {}
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i, arg in enumerate(args):
                if i in types and not isinstance(arg, types[i]):
                    raise TypeError(f"аргумент {i} в диапазоне {types[i]}, {type(arg)}")
                if i in ranges:
                    min_v, max_v = ranges[i]
                    if not min_v <= arg <= max_v:
                        raise ValueError(f"аргумент {i} вне диапазона [{min_v}, {max_v}]")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def make_averager():
    history = []
    
    @validate_args(types={0: (int, float)})
    def averager(*args):
        history.extend(args)
        return sum(history) / len(history)
        
    return averager

if __name__ == "__main__":
    avg = make_averager()
    print(avg(10))
    print(avg(20))
    print(avg(30))
    
    @validate_args(types={0: int}, ranges={0: (1, 10)})
    def test_func(x):
        return x * 2
        
    print(test_func(5))
    try:
        print(test_func(15))
    except Exception as e:
        print(e)
    
