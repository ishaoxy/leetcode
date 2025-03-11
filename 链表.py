class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                return True
        return False

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 反转 left 到right
        p0 = dummy = ListNode(next = head)
        for _ in range(left-1):
            p0 = p0.next
        
        pre = None
        cur = p0.next
        for _ in range(right-left+1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        # 反转结束后，pre指向反转这一段的末尾，cur指向反转这一段后续的下一个节点
        # 结合图像理解这一段代码
        p0.next.next = cur
        p0.next = pre
        return dummy.next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # k个一组反转链表
        # 先统计节点个数
        n = 0
        cur = head
        while cur:
            n+=1
            cur = cur.next
        
        p0 = dummy = ListNode(next = head)
        pre = None
        cur = head
        
        while n>=k:
            n-=k
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            
            # 提前创建一个临时变量nxt = p0.next，前一段重新链接好后更新怕= nxt,开启下一轮循环
            nxt = p0.next
            nxt.next = cur
            p0.next = pre
            p0 = nxt
        return dummy.next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 删除倒数第n个节点 双指针 重点是搞清楚指针的位置
        left = right = dummy = ListNode(next = head)
        for _ in range(n):
            right = right.next #右指针先走n步
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next # 左指针的下一个节点就是倒数第 n 个节点
        return dummy.next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 删除重复元素
        cur = dummy = ListNode(next = head) #dummy节点设置取决于头节点是否可能被删除
        while cur.next and cur.next.next:
            val = cur.next.val
            if cur.next.next.val == val:
                #这里嵌套循环，因为可能存在多个相同的值，需要删干净
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #旋转链表，右移k个位置 先判断长度取余，再快慢指针
        if not head or not head.next:
            return head
        _len = 0
        cur = head
        while cur:
            _len+=1
            cur = cur.next
        k %= _len
        if k==0:
            return head
        slow = fast = head
        while k:
            fast = fast.next
            k-=1
        while fast.next:
            fast = fast.next
            slow = slow.next
        new_head = slow.next
        fast.next = head
        slow.next = None
        return new_head

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 分隔链表，小于x的在前，大于等于x的在后
        dummy1 = p1 = ListNode()
        dummy2 = p2 = ListNode()
        cur = head
        while cur:
            if cur.val<x:
                p1.next = cur
                p1 = p1.next
            else:
                p2.next = cur
                p2 = p2.next
            cur = cur.next
        p1.next = dummy2.next
        p2.next = None
        return dummy1.next


class Node:
    # 提高访问属性的速度，并节省内存 限制类实例能动态添加的属性，从而提高属性访问速度并节省内存；告诉 Python 只为特定的属性分配空间，而不是为每个实例创建一个字典
    __slots__ = 'prev', 'next', 'key', 'value'

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node()
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.key2node = {}

    # 获取 key 对应的节点，同时把该节点移到链表头部
    def get_node(self, key: int) -> Optional[Node]:
        if key not in self.key2node:
            return None
        node = self.key2node[key]
        self.remove(node)
        self.push_front(node)
        return node

    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.value if node else -1
        

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node:
            node.value = value
            return
        self.key2node[key] = node = Node(value=value, key=key)
        self.push_front(node)
        if len(self.key2node) > self.capacity:
            # 删除最久未使用
            back_node = self.dummy.prev
            del self.key2node[back_node.key]
            self.remove(back_node)

    def remove(self, x: Node) -> None:
        x.prev.next = x.next
        x.next.prev = x.prev
    
    def push_front(self, x: Node) -> None:
        x.prev = self.dummy
        x.next = self.dummy.next
        x.prev.next = x
        x.next.prev = x

