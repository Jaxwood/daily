def units_of_water(input: [int]) -> int:
    """You are given an array of non-negative integers that represents a
    two-dimensional elevation map where each element is unit-width wall and
    the integer is the height. Suppose it will rain and all spots between two
    walls get filled up"""
    water = 0
    h = input[0]
    for i in input:
        if i < h:
            water += h - i
        elif i > h:
            h = i
    return water
