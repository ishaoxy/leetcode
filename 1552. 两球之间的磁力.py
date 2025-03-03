class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # 最小磁力最大，二分查找
        def check(d):
            # 当磁力为d时，放置的小球数量是否符合要求
            # 如果 cnt >= m, 说明间距d小，一定能放m个小球
            # 如果 cnt < m, 说明间距d大，放不下m个小球
            cnt = 1
            pre = position[0]
            for p in position:
                if p - pre >= d:
                    cnt += 1
                    pre = p
            return cnt >= m
        
        position.sort()
        left = 0
        # position[0]+(m−1)⋅d ≤ position[n−1]
        right = (position[-1] - position[0])// (m - 1) + 1
        while left + 1 < right:
            mid = (left + right) //2
            if check(mid):
                left = mid
            else:
                right = mid
        return left # 最大的满足能放下m个小球的间距


