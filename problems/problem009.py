def largest_sum(nums):
    """
    Given a list of integers, write a function that returns the largest sum of non-adjacent
    numbers. Numbers can be 0 or negative.
    For example,
    [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
    [5, 1, 1, 5] should return 10, since we pick 5 and 5.
    """
    queue = []
    for i in range(len(nums)):
        queue.append((i+2, nums[i]))

    best = 0
    while len(queue) > 0:
        (i, s) = queue.pop()
        for j in range(i, len(nums)):
            if j < len(nums):
                total = s + nums[j]
                queue.append((j+2, total))
                best = max(best, total)
    return best