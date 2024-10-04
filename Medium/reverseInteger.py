class Solution:
    def reverse(self, x: int) -> int:

        if x == 0:
            return 0

        negative = x < 0
        digits = []
        res = 0

        x = abs(x)

        while x != 0:
            digits.append(str(x % 10))
            x = x // 10

        res = int("".join(digits))

        if res > 2**31 or res < -(2**31):
            return 0

        if negative:
            return -1 * res

        return res
