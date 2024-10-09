class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        a = sorted(nums)

        start = 0
        end = 0

        for i in range(len(nums)):
            if a[i] != nums[i]:
                start = i
                break

        for i in range(len(nums)):
            if a[len(nums) - i - 1] != nums[len(nums) - i - 1]:
                end = len(nums) - i
                break

        return end - start
