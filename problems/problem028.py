import math
def justify(s: [str], k: int) -> [str]:
    """Write an algorithm to justify text. Given a sequence of words and an
    integer line length k, return a list of strings which represents each
    line, fully justified."""
    lines = []
    sentence = []
    # group words into lines
    while len(s) > 0:
        f = s.pop(0)
        l = len(' '.join(sentence))
        if len(f) + l + 1 <= k:
            sentence.append(f)
        else:
            lines.append(sentence)
            sentence = []
            sentence.append(f)
    lines.append(sentence)

    # justify the line
    for line in lines:
        length = len(''.join(line))
        whitespaces = k - length
        idx = 0
        while whitespaces > 0:
            line[idx] = line[idx] + ' '
            whitespaces -= 1
            if idx + 1 >= len(line) - 1:
                idx = 0
            else:
                idx += 1

    # merge lines
    result = []
    for line in lines:
        result.append(''.join(line))
    return result
