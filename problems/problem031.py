def edit_distance(a: str, b: str) -> int:
    """Given two strings, compute the edit distance between them."""
    cnt = 0
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            cnt += 1
    return cnt + max(len(a), len(b)) - min(len(a), len(b))
