class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 验证回文串
        # 正则
        # import re
        # s = s.lower()
        # char = r'[a-z0-9]'
        # s = re.findall(char,s)
        # s = "".join(s)
        # if s =="":
        #     return True
        # else:
        #     return s==s[::-1]
        
        #双指针
        i,j = 0,len(s)-1
        while i<j:
            if not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
            elif s[i].lower()==s[j].lower():
                i+=1
                j-=1
            else:
                return False
        return True
        

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #判断子序列
        if not s:
            return True
        i = 0
        for value in t:
            if s[i]==value:
                i+=1
                if i==len(s):
                    return True
        return False
    

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #两数之和
        left = 0
        right = len(numbers)-1
        while True:
            s = numbers[left]+numbers[right]
            if s==target:
                return [left+1,right+1]
            if s<target:
                left+=1
            else:
                right -=1

class Solution:
    def maxArea(self, height: List[int]) -> int:
        #乘最多水的容器
        l,r = 0,len(height)-1
        ans = 0
        while l<r:
            area = min(height[l],height[r])*(r-l)
            ans = max(ans,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return ans
    
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #三数之和
        n = len(nums)
        res = []
        if (not nums or n<3):
            return[]
        nums.sort()
        for i in range(n):
            if(nums[i]>0):
                return res
            if(i>0 and nums[i]==nums[i-1]):
                continue
            l =i+1
            r = n-1
            while(l<r):
                if(nums[i]+nums[l]+nums[r]==0):
                    res.append([nums[i],nums[l],nums[r]])
                    while(l<r and nums[l]==nums[l+1]):
                        l+=1
                    while(l<r and nums[r]==nums[r-1]):
                        r-=1
                    l+=1
                    r-=1
                elif(nums[i]+nums[l]+nums[r]>0):
                    r-=1
                else:
                    l+=1
        return res
