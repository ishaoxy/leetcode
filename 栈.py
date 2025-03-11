class Solution:
    def isValid(self, s: str) -> bool:
        # 有效的括号
        dic = {'{':'}','[':']','(':')','?':'?'}
        stack = ['?']
        
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()]!=c:# 如果栈顶元素对应的右括号不等于当前字符，提前返回False  同时设置“？”是为了防止栈为空时pop报错
                return False
        return len(stack) == 1

class Solution:
    def simplifyPath(self, path: str) -> str:
        # 简化路径
        # 给你一组由 / 隔开的字符串（忽略空串和 .），请你从左到右遍历这些字符串，依次删除每个 .. 及其左侧的字符串
        stack=[]
        for s in path.split('/'):
            if s == "" or s ==".":
                continue
            if s !="..":
                stack.append(s)
            elif stack:
                stack.pop()
        return "/" + "/".join(stack)


class MinStack:
    # 最小栈，利用辅助栈，每次入栈时，同时入栈当前最小值

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val,val))
        else:
            self.stack.append((val,min(val,self.stack[-1][1])))        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 逆波兰表达式
        stack = []
        for token in tokens:
            try:
                stack.append(int(token))
            except:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(self.evaluate(num1,num2,token))
        return stack[0]
    
    def evaluate(self,num1,num2,token):
        if token =="+":
            return num1+num2
        elif token == "-":
            return num1-num2
        elif token == "*":
            return num1*num2
        else:
            return int(num1/float(num2))