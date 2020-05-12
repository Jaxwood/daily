from functools import reduce

def products(arr):
  """Given an array of integers, return a new array
  such that each element at index i of the new array
  is the product of all the numbers in the original array
  except the one at i"""
  result = []
  res = reduce((lambda a, n: a * n), arr, 1)
  for a in arr:
    result.append(res / a)
  return result