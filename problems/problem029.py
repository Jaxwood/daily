def encode(s: str) -> str:
    """Run-length encoding is a fast and simple method of encoding strings.
    The basic idea is to represent repeated successive characters as a single
    count and character."""
    result = ''
    prev = s[:1]
    cnt = 0
    for c in s:
        if c == prev:
            cnt += 1
        else:
            result += str(cnt) + prev
            prev = c
            cnt = 1
    result += str(cnt) + prev

    return result


def decode(s: str) -> str:
    cnt = 0
    result = ''
    for c in s:
        if c.isdigit():
            cnt = int(c)
        else:
            for _ in range(cnt):
                result += c
    return result
