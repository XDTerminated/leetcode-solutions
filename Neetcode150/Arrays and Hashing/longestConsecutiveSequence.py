class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        x = list(set(nums))
        x.sort()
        a = x[0]
        counts = []
        count = 1
        for i in range(len(x) - 1):
            if x[i + 1] - a == 1:
                a = x[i + 1]
                count+=1

            else:
                counts.append(count)
                a = x[i + 1]
                count = 1

        counts.append(count)

        return max(counts)
