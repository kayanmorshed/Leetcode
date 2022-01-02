class Solution:
    def checkString(self, s: str) -> bool:
        if len(s) == 1: return True
        return not (s.find('ba') > -1)
        