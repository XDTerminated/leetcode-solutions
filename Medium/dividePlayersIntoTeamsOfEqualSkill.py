class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        a = 0
        b = len(skill) - 1

        skillSum = skill[a] + skill[b]
        res = 0

        while a < b:
            if skill[a] + skill[b] == skillSum:
                res += skill[a] * skill[b]

            else:
                return -1
            a += 1
            b -= 1

        return res
