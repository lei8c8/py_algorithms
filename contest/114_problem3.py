class Solution:

    def minDeletionSize(self, A):
        res, n, = 0, len(A)
        cur = [""] * n
        for col in zip(*A):
            cur2 = [None] * n
            for i in range(n):
                cur2[i] = cur[i] + col[i]
            if cur2 == sorted(cur2):
                cur = cur2
            else:
                res += 1
        return res

s = Solution()
data = ["xga","xfb","yfa"]
result = s.minDeletionSize(data)
print(result)