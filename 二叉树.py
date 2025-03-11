class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 翻转二叉树
        if not root:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) ->bool:
        if p is None or q is None:
            return p==q
        return p.val==q.val and self.isSameTree(p.left,q.right) and self.isSameTree(p.right,q.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 对称二叉树
        return self.isSameTree(root.left,root.right)
    
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 先序与中序构建二叉树
        if not preorder:
            return None
        left_size = inorder.index(preorder[0])
        left = self.buildTree(preorder[1:left_size+1],inorder[:left_size])
        right = self.buildTree(preorder[left_size+1:],inorder[left_size+1:])
        return TreeNode(preorder[0],left,right)

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #  中序与后序
        if not postorder:
            return None
        left_size = inorder.index(postorder[-1])
        left = self.buildTree(inorder[:left_size],postorder[:left_size])
        right = self.buildTree(inorder[left_size+1:],postorder[left_size:-1])
        return TreeNode(postorder[-1],left,right)

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # 填充每个节点的下一个右侧节点指针
        cur = root
        while cur:
            nxt = dummy = ListNode(0)
            while cur:
                if cur.left:
                    nxt.next = cur.left
                    nxt = cur.left
                if cur.right:
                    nxt.next = cur.right
                    nxt = cur.right
                cur = cur.next
            cur = dummy.next
        return root

class Solution:
    head = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 二叉树展开为链表
        # 头插法
        if root is None:
            return 
        self.flatten(root.right)
        self.flatten(root.left)
        root.left = None
        root.right = self.head
        self.head = root
    

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 路径总和
        if not root:
            return False
        targetSum -= root.val
        if root.left is root.right:
            return targetSum ==0
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)

class Solution:
    def sumNumbers(self, root: Optional[TreeNode], x=0) -> int:
        # 求根到叶子节点数字之和
        if not root:
            return 0
        x = x*10 + root.val
        if root.left is root.right:
            return x
        return self.sumNumbers(root.left,x)+self.sumNumbers(root.right,x)

class Solution:
    def height(self,root):
        height = 0
        while root:
            root = root.left
            height+=1
        return height
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # 完全二叉树的节点个数
        if not root:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        if left_height == right_height:
            return (2**left_height-1)+ self.countNodes(root.right)+1
        else:
            return (2**right_height-1)+self.countNodes(root.left)+1

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 最近公共祖先
        if root in (None,p,q):
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        return left or right