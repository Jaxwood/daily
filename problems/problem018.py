def maximum_value(arr: [int], k: int) -> [int]:
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