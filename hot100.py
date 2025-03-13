class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 移动零 双指针
        i0 = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i],nums[i0] = nums[i0],nums[i]
                i0+=1

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 无重复字符的最长子串
        # 哈希表 整形数组
        ans = left = 0
        cnt = defaultdict(int) #defaultdict是collections模块中的一个子类，它会为你提供一个默认值。当你访问一个不存在的键时，它会自动创建这个键并赋予一个默认值（例如0）
        # cnt = {}
        for right,c in enumerate(s):
            cnt[c]+=1
            while cnt[c]>1:
                cnt[s[left]]-=1
                left+=1
            ans = max(ans,right-left+1)
        return ans
    
        # 哈希集合 布尔数组
        ans = left = 0
        window = set()
        for right,c in enumerate(s):
            while c in window:
                window.remove(s[left])
                left+=1
            window.add(c)
            ans = max(ans,right-left+1)
        return ans

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 找到字符串中所有字母异位词
        # 滑动窗口
        ans = []
        cnt = Counter(p)
        left = 0
        for right,c in enumerate(s):
            cnt[c]-=1
            while cnt[c]<0:
                cnt[s[left]]+=1
                left+=1
            if right-left+1 ==len(p):
                ans.append(left)
        return ans

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #相交链表 (x+z)+y=(y+z)+x
        pa,pb = headA,headB
        while pa is not pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 反转链表
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 回文链表
        # 快慢指针 倒排
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        pre = None
        while slow:
            nxt = slow.next
            slow.next = pre
            pre = slow
            slow = nxt
        
        while pre:
            if pre.val != head.val:
                return False
            pre = pre.next
            head = head.next
        return True

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #环形链表进阶 重点是搞清楚数学证明关系
        slow = fast = head
        while True:
            if not fast or not fast.next:
                return None
            
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                break

        ptr = head
        while ptr!=slow:
            ptr = ptr.next
            slow = slow.next
        return ptr