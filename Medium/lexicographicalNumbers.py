# Using bfs

# class Solution:
#     def lexicalOrder(self, n: int) -> list[int]:
#         return self.bfs(1, n)

#     def bfs(self, current, max):
#         l = []
#         for i in range(current, (current + 10) - (current + 10)):
#             print(i)
#             if i > max:
#                 return l

#             l.append(i)
#             l = l + self.bfs(i * 10, max)


#         return l

class Solution:
    def lexicalOrder(self, n: int) -> list[int]:

        res = []
        cur = 1

        while len(res) < n:
            res.append(cur)

            if cur * 10 <= n:
                cur = cur * 10

            else:
                while cur == n or cur%10 == 9:
                    cur = cur//10

                cur += 1

        return res
