class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Using Regex
        # s = re.sub(r'[\W_]+',"",s).lower()
        # reverse = s[::-1]
        # return s == reverse

        # Using pointers
        s = s.lower()
        pointerStart = 0
        pointerEnd = len(s) - 1

        s1 = ""
        s2 = ""

        while pointerEnd >= 0:
            if s[pointerStart].isalnum():
                s1 += s[pointerStart]
            if s[pointerEnd].isalnum():
                s2 += s[pointerEnd]
            pointerStart += 1
            pointerEnd -= 1


        return s1 == s2
