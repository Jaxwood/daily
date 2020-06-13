def median(xs: [int]) -> [int]:
    """Compute the running median of a sequence of numbers. That is, given a
    stream of numbers, print out the median of the list so far on each new
    element"""
    sofar = []
    result = []
    for i in xs:
        sofar.append(i)
        sofar.sort()
        if len(sofar) == 1:
            result.append(sofar[0])
        elif len(sofar) == 2:
            result.append(sum(sofar) / 2)
        else:
            candidates = sofar[1:-1]
            while len(candidates) > 2:
                candidates = candidates[1:-1]
            if len(candidates) == 1:
                result.append(candidates[0])
            else:
                result.append(sum(candidates) / 2)
    return result
