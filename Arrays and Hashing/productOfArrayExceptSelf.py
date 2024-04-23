class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1] * len(nums)
        suf = 1
        for i in range(len(nums) - 1):
            arr[i + 1] = nums[i]*arr[i]

        for i in range(len(nums) - 1, -1, -1):
            arr[i] = arr[i] * suf
            suf = suf * nums[i]

        return arr