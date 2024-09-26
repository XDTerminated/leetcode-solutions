class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        index = 0
        direction = 1
        for i in range(k):
            if direction == 1:
                index += 1
            else:
                index-=1

            if index == n - 1:
                direction = -1

            if index == 0:
                direction = 1


        return index
