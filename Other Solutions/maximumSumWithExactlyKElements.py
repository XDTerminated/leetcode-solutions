class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        res = 0

        maxIndex = 0
        for i in range(len(nums)):
            if nums[maxIndex] < nums[i]:
                maxIndex = i

        for i in range(k):
            res+=nums[maxIndex]
            nums[maxIndex] += 1

        return res
