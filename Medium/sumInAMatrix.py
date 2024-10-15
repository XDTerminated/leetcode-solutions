class Solution:
    def matrixSum(self, nums: list[list[int]]) -> int:

        for i in range(len(nums)):
            nums[i].sort()

        score = 0
        for i in range(len(nums[0])):
            max_val = 0
            for j in range(len(nums)):
                if nums[j][i] > max_val:
                    max_val = nums[j][i]

            score += max_val

        return score
