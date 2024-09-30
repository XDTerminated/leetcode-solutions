class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        pointerDuplicate = 0
        pointerUnique = 0
        l = len(nums)
        while pointerDuplicate < l:
            if nums[pointerDuplicate] != nums[pointerUnique]:
                pointerUnique += 1
                nums[pointerUnique] = nums[pointerDuplicate]
                pointerDuplicate += 1
            else:
                pointerDuplicate += 1

        return pointerUnique + 1

        # Pythonic Solution
        nums[:] = sorted(set(nums))
