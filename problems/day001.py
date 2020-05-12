
def hasSumOfPair(numbers, k):
  numbers.sort()
  i = 0
  j = len(numbers) - 1
  while(True):
    if (i >= j):
      return False
    if (numbers[i] + numbers[j] == k):
      return True
    if (numbers[i] + numbers[j] > k):
      j-= 1
      continue
    if (numbers[i] + numbers[j] < k):
      i+= 1
      continue