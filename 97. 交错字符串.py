class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m   = len(s1), len(s2)
        if n + m != len(s3):
            return False
        
        @cache 
        def dfs(i,j):
            # i , j 分别代表s1和s2最后一个字母的下标
            if i < 0 and j < 0:
                return True
            return i >= 0 and s1[i] == s3[i + j + 1] and dfs(i - 1,j) or j >= 0 and s2[j] == s3[i + j + 1] and dfs(i,j - 1)
        
        return dfs(n - 1,m - 1)