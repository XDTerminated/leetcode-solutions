class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        l = [i + 1 for i in range(k)]

        count = 0

        for i in range(len(nums) - 1, -1, -1):
            if len(l) == 0:
                break

            if nums[i] in l:
                l.remove(nums[i])

            count += 1

        return count
