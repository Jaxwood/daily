def schedule(classes: [(int, int)]) -> int:
    """Given an array of time intervals (start, end) for classroom lectures
    (possibly overlapping), find the minimum number of rooms required"""
    # sort on start then end time
    classes.sort(key=lambda a: a[0])
    classes.sort(key=lambda a: a[1])
    # pick the first class
    (_, end) = classes[0]
    non_overlapping = 1
    idx = 0
    while len(classes) > idx:
        start = classes[idx][0]
        # check start time
        if start > end:
            end = classes[idx][1]
            non_overlapping += 1
        idx += 1
    return non_overlapping
