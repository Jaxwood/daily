def units_of_water(arr: [int]) -> int:
    """You are given an array of non-negative integers that represents a
    two-dimensional elevation map where each element is unit-width wall and
    the integer is the height. Suppose it will rain and all spots between two
    walls get filled up"""
    if not arr:
        return 0

    total = 0
    max_i = arr.index(max(arr))

    left_max = arr[0]
    for num in arr[1:max_i]:
        total += left_max - num
        left_max = max(left_max, num)

    right_max = arr[-1]
    for num in arr[-2:max_i:-1]:
        total += right_max - num
        right_max = max(right_max, num)

    return total
