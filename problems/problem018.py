def maximum_value(arr: [int], k: int) -> [int]:
    """Given an array of integers and a number k, where 1 <= k <= length of
    the array, compute the maximum values of each subarray of length k."""
    m = []
    res = []
    for i in range(len(arr)):
        if len(m) == k:
            res.append(max(m))
        if len(m) == k:
            m[i%k] = arr[i]
        else:
            m.append(arr[i])
    res.append(max(m))
    return res