class Solution:

    def encode(self, strs: List[str]) -> str:
        a = ""
        for i in range(len(strs)):
            a+=strs[i] + ":;:;:;:"

        return a

    def decode(self, s: str) -> List[str]:
        return s.split(":;:;:;:")[0:-1]
