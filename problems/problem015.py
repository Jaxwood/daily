from random import randint


def stream(num):
    """Given a stream of elements too large to store in memory, pick a random
    element from the stream with uniform probability"""
    n = 100000
    total = 0
    for i in generate(n):
        if i == num:
            total += 1
    return round(total / n, 3)


def generate(times):
    """simulate a stream of uniform elements, e.g. dice rolls"""
    while times > 0:
        yield randint(1, 6)
        times -= 1
