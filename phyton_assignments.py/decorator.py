from time import time


def time_taken(func):
    def wrap(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"it took {t2 - t1 : .3f}ms to execute")
        return result

    return wrap

