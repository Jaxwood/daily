class Bracket:
    Unknown = 0
    Curly = 1
    Round = 2
    Square = 3

def well_formed(s: str) -> bool:
    """Given a string of round, curly, and square open and closing brackets,
    return whether the brackets are balanced (well-formed)."""
    history = []
    curly, round, square = 0, 0, 0
    for c in s:
        if c == '{':
            curly += 1
            history.append(Bracket.Curly)
        if c == '[':
            square += 1
            history.append(Bracket.Square)
        if c == '(':
            round += 1
            history.append(Bracket.Round)
        if c == '}':
            curly -= 1
            if curly == 0 and history.pop() != Bracket.Curly:
                return False
        if c == ']':
            square -= 1
            if square == 0 and history.pop() != Bracket.Square:
                return False
        if c == ')':
            round -= 1
            if round == 0 and history.pop() != Bracket.Round:
                return False
    return curly == 0 and square == 0 and round == 0
