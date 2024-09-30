class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        countRight = 0
        countLeft = 0

        found = False
        found2 = False

        a = start

        while start < len(nums):
            if nums[start] == target:
                found = True
                break

            countRight+=1
            start+=1

        while a >= 0:
            if nums[a] == target:
                found2 = True
                break

            countLeft+=1
            a-=1

        if not found:
            countRight = (1000 + countLeft) * 2

        if not found2:
            countLeft = (1000 + countRight) * 2

        return min(countRight, countLeft)
