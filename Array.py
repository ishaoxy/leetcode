class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k+=1
        return k    
    

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n -1
        while p2 >= 0:
            if p1 >=0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums1[p2]
                p2 -=1
            p -= 1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1,len(nums)):
            if nums[i] !=nums [i-1]:
                nums[k] = nums[i]
                k+=1
        return k
        
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 快慢指针
        slow = 0
        for fast in range(len(nums)):
            if slow <2 or nums[fast] !=nums[slow-2]:
                nums[slow] = nums[fast]
                slow+=1
        return slow

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # return nums[len(nums)//2]

        # 摩尔投票法
        votes = 0
        for num in nums:
            if votes == 0:
                x = num
            votes+=1 if num ==x else -1
        return x
    
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 三次翻转
        def reverse(i,j):
            while i<j:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j-=1
        
        n = len(nums)
        k %=n
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost, profit = float('+inf'), 0
        for price in prices:
            cost = min(cost,price)
            profit = max(profit,price-cost)
        return profit
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1,len(prices)):
            tmp = prices[i] - prices[i-1]
            if tmp > 0:
                profit += tmp
        return profit

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_i = 0
        for i,jump in  enumerate(nums):
            if max_i >= i and i+jump >max_i:
                max_i = i+jump
        return max_i >= i

class Solution:
    def jump(self, nums: List[int]) -> int:
        # 跳到nums[n-1]的最小次数
        ans = 0
        cur_right = 0
        next_right = 0
        for i in range(len(nums) - 1):
            next_right = max(next_right,i+nums[i])
            if i == cur_right:
                cur_right = next_right
                ans +=1
        return ans
    
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 加油站
        ans = min_s = s = 0 # s为当前油量,min_s为最小油量
        for i ,(g,c) in enumerate(zip(gas,cost)):
            s +=g - c
            if s < min_s:
                min_s = s #更新最小油量
                ans = i +1 #s-c后，汽车在i+1
        return -1 if s<0 else ans

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 分发糖果，其实就是前后两次遍历了，分别满足左规则右规则
        left = [1]*len(ratings)
        right  = left[:]
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1]+1
        count = left[-1]

        for i in range(len(ratings)-2, -1,-1):
            if ratings[i]>ratings[i+1]:
                right[i] = right[i+1]+1
            count += max(left[i],right[i])
        return count

class Solution:
    def trap(self, height: List[int]) -> int:
        # 接雨水，前后缀分解
        n = len(height)
        pre_max = [0]*n
        pre_max[0] = height[0]
        for i in range(1,n):
            pre_max[i] = max(pre_max[i-1],height[i])
        
        suf_max = [0]*n
        suf_max[-1] = height[-1]
        for i in range(n-2,-1,-1):
            suf_max[i] = max(suf_max[i+1],height[i])
        
        ans = 0
        for h,pre,suf in zip(height,pre_max,suf_max):
            ans += min(pre,suf)-h
        return ans

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # h指数
        n = len(citations)
        cnt = [0]*(n+1)
        for c in citations:
            cnt[min(n,c)]+=1 #超过数组长度，就只记为n
        s = 0
        for i in range(n,-1,-1):
            s+=cnt[i]
            if s>=i:
                return i

from itertools import pairwise
ROMAN = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        for x,y in pairwise(s):
            if ROMAN[x]>=ROMAN[y]:
                ans +=ROMAN[x]
            else:
                ans -=ROMAN[x]
        return ans + ROMAN[s[-1]]


# 大表解决
R = (("","I","II","III","IV","V","VI","VII","VIII","IX"),
     ("","X","XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"),
     ("","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"),
     ("","M","MM","MMM"),

)
class Solution:
    def intToRoman(self, num: int) -> str:
        return R[3][num//1000]+R[2][num//100%10]+R[1][num//10%10]+R[0][num%10]
    

#贪婪算法
class Solution:
    def intToRoman(self, num: int) -> str:
        roma_dict = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC',
         100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
        roma_nums = list(roma_dict.keys())
        roma_ans = []

        for val in roma_nums[::-1]:
            while num>=val:
                num -=val
                roma_ans.append(roma_dict[val])
        return "".join(roma_ans)
        
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #暴力即优雅 O(mn)
        s0 = strs[0]
        for j,c in enumerate(s0):
            for s in strs:
                if j==len(s) or s[j]!=c:
                return s0[:j]
        return s0