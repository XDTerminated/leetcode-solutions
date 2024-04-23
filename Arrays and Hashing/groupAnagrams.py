class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        b = defaultdict(list)
        for i in range(len(strs)):
            x = "".join(sorted(strs[i]))
            b[x].append(strs[i])


        return b.values()