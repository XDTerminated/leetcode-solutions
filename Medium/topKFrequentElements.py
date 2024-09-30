class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        for i in range(len(nums)):
            hm[nums[i]] += 1

        print(hm)
        ans = []
        x = sorted(hm.items(), key=lambda x:x[1])[::-1]
        for i in range(k):
            ans.append(x[i][0])

        return ans