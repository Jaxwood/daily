def cons(a, b):
    """cons(a, b) constructs a pair"""
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    """car(pair) returns the first element of that pair"""
    return pair((lambda a,b: a))


def cdr(pair):
    """cdr(pair) returns the last element of that pair"""
    return pair((lambda a,b: b))
