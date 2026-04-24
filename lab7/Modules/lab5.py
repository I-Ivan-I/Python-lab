import functools

def validate_args(types=None, ranges=None):
    types = types or {}
    ranges = ranges or {}

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i, arg in enumerate(args):
                if i in types and not isinstance(arg, types[i]):
                    raise TypeError(f"Argument {i} type error")
                if i in ranges:
                    min_v, max_v = ranges[i]
                    if not min_v <= arg <= max_v:
                        raise ValueError(f"Argument {i} range error")
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