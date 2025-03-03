class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        @cache
        def dfs(i,j):
            if i<0:
                return j+1
            if j<0:
                return i+1
            if word1[i] == word2[j]:
                return dfs(i-1,j-1)
            return min(dfs(i - 1,j), dfs(i, j-1), dfs(i - 1, j - 1)) + 1 # 对应三种操作 删除 插入 替换 再加上本次操作次数
        return dfs(n-1,m-1)