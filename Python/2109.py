class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        sub_str = []
        prev = 0
        for space in spaces:
            sub_str.append(s[prev:space])
            prev = space
        sub_str.append(s[prev:])
        return " ".join(sub_str)
        