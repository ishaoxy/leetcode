class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:#
        # 最小化最大值
        # 二分查找
        def check(m):
            cnt = 0
            for num in nums:
                cnt += (num - 1) // m
            return cnt <= maxOperations
    
        left = 0  # 循环不变量 check(left) = False
        right = max(nums) # 循环不变量 check(right) = True
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right
