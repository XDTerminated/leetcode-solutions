# class Solution:
#     def minLength(self, s: str) -> int:
#         if "AB" not in s and "CD" not in s:
#             return len(s)

#         s = s.replace("AB", "").replace("CD", "")
#         return self.minLength(s)


class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
                continue
            if s[i] == "B" and stack[-1] == "A":
                stack.pop()

            elif s[i] == "D" and stack[-1] == "C":
                stack.pop()

            else:
                stack.append(s[i])

        return len(stack)
