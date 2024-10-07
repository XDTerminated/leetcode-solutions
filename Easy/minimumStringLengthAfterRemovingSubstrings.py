class Solution:
    def minLength(self, s: str) -> int:
        if "AB" not in s and "CD" not in s:
            return len(s)

        s = s.replace("AB", "").replace("CD", "")
        return self.minLength(s)
