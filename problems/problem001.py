
def hasSumOfPair(numbers, k):
    """Given a list of numbers and a number k,
    return whether any two numbers from the list add up to k."""
    numbers.sort()
    i = 0
    j = len(numbers) - 1
    while(True):
        if (i >= j):
            return False
        if (numbers[i] + numbers[j] == k):
            return True
        elif (numbers[i] + numbers[j] > k):
            j -= 1
        elif (numbers[i] + numbers[j] < k):
            i += 1
