from random import random
from math import sqrt

def monte_carlo(total: int) -> float:
  """The area of a circle is defined as πr^2. Estimate π to 3 decimal places
  using a Monte Carlo method."""
  inside = 0
  for _ in range(total):
    # random x and y between 0-1
    x = random()
    y = random()
    # for a circle with radius 0.5
    # check if inside the circle
    # x^2 + y^2 = r^2, e.g. r = sqrt(x^2 + y^2)
    if sqrt(x * x + y * y) < 0.5:
      inside += 1
  # area for circle is pi*0.5^2 = pi/4.
  # area = inside / total
  area = 4 * inside / total
  # given the formular for an area for a circle
  # e.g. area = pi*r^2 and our radius of 0.5
  # pi = area * 4
  return round(4*area, 3)