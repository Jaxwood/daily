def words(w: [str], s: str) -> str:
    """Given a dictionary of words and a string made up of those words (no
    spaces), return the original sentence in a list. If there is more than
    one possible reconstruction, return any of them. If there is no possible
    reconstruction, then return null."""
    sentence = []
    idx = 0
    while len(s) > 0:
        if s.find(w[idx]) == 0:
            s = s[len(w[idx]):]
            sentence.append(w[idx])
            idx = 0
        else:
            idx += 1
        if idx == len(w):
            return None
    return sentence
