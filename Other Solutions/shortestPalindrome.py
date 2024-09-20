class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == "":
            return ""

        reversedS = s[::-1]
        matched = ""


        for i in range(len(s)):
            if reversedS[i::] == s[0:len(s) - i]:
                matched = reversedS[i::]
                return reversedS[0:i] + matched + s[len(s) - i::]
