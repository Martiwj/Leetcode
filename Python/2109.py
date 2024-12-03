class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        sub_str = []
        prev = 0
        for space in spaces:
            st = s[prev:space]
            sub_str.append(st)
            prev = space
        sub_str.append(s[prev:])
        return " ".join(sub_str)
        