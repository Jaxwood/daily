def unique_counter(s):
    if s.startswith('0'):
        return 0
    elif len(s) <= 1:
        return 1

    total = 0

    if int(s[:2]) <= 26:
        total += unique_counter(s[2:])

    total += unique_counter(s[1:])
    return total
