import re


class Solution:
    def myAtoi(self, s: str) -> int:
        parse = re.search("(^ *\d+)|(^ *\+\d+)|(^ *-\d+)", s)
        if not parse:
            return 0

        integer = int(parse.group())

        if integer < 0:
            return max((-2) ** 31, integer)
        else:
            return min(2**31 - 1, integer)
