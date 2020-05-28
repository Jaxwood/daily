import re
def longest_path(s: str, separator: str, total = 0) -> str:
  if s.find(separator) == -1:
    return s

  for i in s.split(separator):
    if i.find('\t') == -1:
      print('match', i)
    else:
      return longest_path(i, separator + '\t')


# "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"