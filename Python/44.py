import re

def isMatch(s, p):
    pattern = rf'\b{re.escape(p)}\b'
    match = re.search(pattern, s)
    return match is not None

print(isMatch("aa", "*"))
