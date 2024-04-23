class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # Another way to do the problem

        # h = defaultdict(int)
        # for i in nums:
        #     h[i] += 1
        #     if (h[i]) > 1:
        #         return True

        # return False

        nums.sort()
        for i in range(len(nums) - 1):
            if (nums[i] + nums[i + 1])/2 == nums[i]:
                return True

        return False