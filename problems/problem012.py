async def stairs(n):
    """There exists a staircase with N steps, and you can climb up either 1
    or 2 steps at a time. Given N, write a function that returns the number
    of unique ways you can climb the staircase. The order of the steps
    matters."""
    if n == 0:
        return 1
    if n < 0:
        return 0
    return stairs(n-1) + stairs(n-2)