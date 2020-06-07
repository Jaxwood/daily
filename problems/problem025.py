def matches_first_char(s, r):
    return s[0] == r[0] or (r[0] == '.' and len(s) > 0)

def matches(s, r):
    """implement a function that takes in a string and a valid regular
    expression and returns whether or not the string matches the regular
    expression."""
    if r == '':
        return s == ''

    if len(r) == 1 or r[1] != '*':
        # The first character in the regex is not proceeded by a *.
        if matches_first_char(s, r):
            return matches(s[1:], r[1:])
        else:
            return False
    else:
        # The first character is proceeded by a *.
        # First, try zero length.
        if matches(s, r[2:]):
            return True
        # If that doesn't match straight away, then try globbing more prefixes
        # until the first character of the string doesn't match anymore.
        i = 0
        while matches_first_char(s[i:], r):
            if matches(s[i+1:], r[2:]):
                return True
            i += 1