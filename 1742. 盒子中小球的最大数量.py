class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        # 暴力枚举
        cnt = Counter(
            sum(int(c) for c in str(i)) for i in range(lowLimit, highLimit + 1)
        )
        return max(cnt.values())
    

s = [[0] * 46]
for i in range(1, 100001):
    j = sum(int(c) for c in str(i))
    s.append(s[i - 1][:])
    s[i][j] += 1   
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:       
       # 前缀和
       # s[i][j] 表示 [0, i] 中数字和为 j 的个数
       # s[highLimit][j] - s[lowLimit - 1][j] 
       # 遍历 j 从 1 到 45
       return max(s[highLimit][j] - s[lowLimit - 1][j] for j in range(1, 46))

       
    
