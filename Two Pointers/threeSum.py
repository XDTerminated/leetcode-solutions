class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if nums[i] == nums[i - 1] and i > 0:
                continue

            target = -1 * nums[i]
            a = i + 1
            b = len(nums) - 1

            while a < b:

                s = nums[a] + nums[b]

                if s == target:
                    ans.append([nums[i], nums[a], nums[b]])

                    a+=1
                    b-=1

                    while nums[a] == nums[a - 1] and a < b:
                        a = a + 1

                    while a < b and nums[b] == nums[b + 1]:
                        b = b-1

                elif s < target:
                    a+=1

                elif s > target:
                    b -= 1



        return ans
