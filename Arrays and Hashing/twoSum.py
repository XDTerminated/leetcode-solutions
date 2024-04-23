class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_idx_map = {}
        for j, x in enumerate(nums):
            compliment = target - x
            if compliment in value_idx_map:
                return (j, value_idx_map[compliment])
            else:
                value_idx_map[x] = j