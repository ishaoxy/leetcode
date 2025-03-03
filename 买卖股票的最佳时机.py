class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit  = 0
        for i in range(1, len(prices)):
            tmp = prices[i] = prices[i-1]
            if tmp>0:
                profit +=tmp
        return profit
    
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # 至多交易k次
        n = len(prices)
        @cache
        def dfs(i,j,hold):
            if j<0:
                return -inf
            if i<0:
                return -inf if hold else 0
            if hold:
                # 如果持有，计算 继续持有或卖出
                return max(dfs(i-1,j,True),dfs(i-1,j-1,False)-prices[i])
            # 如果不持有，计算 继续不持有或买入
            return max(dfs(i-1,j,False),dfs(i-1,j,True)+prices[i])
        return dfs(n-1,k,False)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 最多交易两次
        k = 2
        f = [[-inf]*2 for _ in range(k+2)]:
        for j in range(1,k+2):
            f[j][0] = 0
        for p in prices:
            for j in range(k+1,0,-1):
                f[j][0] = max(f[j][0],f[j][1]+p)
                f[j][1] = max(f[j][1],f[j-1][0]-p)
        return f[-1][0]