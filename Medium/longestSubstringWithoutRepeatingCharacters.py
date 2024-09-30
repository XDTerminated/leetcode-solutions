class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        if len(s) == 1:
            return 1

        maxSubstring = ""
        pointerLeft = 0
        pointerRight = 1

        for i in range(len(s)):
            if len(s[pointerLeft:pointerRight]) == len(set(s[pointerLeft:pointerRight])):
                maxSubstring = s[pointerLeft:pointerRight]
                pointerRight += 1
            else:
                pointerRight+=1
                pointerLeft+=1

        return len(maxSubstring)
