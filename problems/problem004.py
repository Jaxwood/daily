def missing(input):
    """Given an array of integers, find the first missing positive
    integer in linear time and constant space. In other words,
    find the lowest positive integer that does not exist in the array.
    The array can contain duplicates and negative numbers as well."""
    a = set(input) # space is O(N) and not constant as the problem states :<
    for i in range(len(input)):
        if not (i+1) in a:
            return i + 1
    return len(input) + 1

def missing_optimized(input):
    """same as above - but honor the constant space requirement"""
    for i in range(len(input)):
        cnt = i
        while cnt < len(input):
            if (input[cnt] == i + 1):
                input[i], input[cnt] = input[cnt], input[i]
                break
            cnt += 1
            if (cnt >= len(input)):
                return i + 1
    return len(input) + 1