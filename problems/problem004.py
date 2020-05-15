def missing(input):
    """Given an array of integers, find the first missing positive
    integer in linear time and constant space. In other words,
    find the lowest positive integer that does not exist in the array.
    The array can contain duplicates and negative numbers as well."""
    a = set(input)
    for i in range(len(input)):
        if not (i+1) in a:
            return i + 1
    return len(input) + 1