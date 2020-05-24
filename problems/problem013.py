def distinct_sequence(k: int, s: str) -> int:
  """Given an integer k and a string s, find the length of the longest
  substring that contains at most k distinct characters. For example, given s
  = "abcba" and k = 2, the longest substring with k distinct characters is
  "bcb".
  """
  best = 0
  for i in range(len(s)):
    candidate = s[i]
    for j in range(i+1, len(s)):
      if len(candidate) < 2:
        candidate += s[j]
      elif s[j] in set(candidate):
          candidate += s[j]
      else:
        break
    best = max(len(candidate), best)
  return best