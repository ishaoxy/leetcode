class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # colors 0还未访问
        # colors 1访问中
        # colors 2已经访问完成
        # 标记正在访问，查找邻居，如果邻居colors = 1,即有环，TRUE
                               # 如果邻居colors = 0,dfs(y)=TRUE,则dfs(x)也为TRUE
                               # 没找到，colors[x] = 2,返回false
        # 查看dfs(x),如果找到环TRUE,最后返回FALSE
        # 如果所有都返回FALSE,即没有环，返回TRUE
        g = [[] for _ in range (numCourses)] 
        for a,b in prerequisites:
            g[b].append(a)
        
        colors = [0]*numCourses
        def dfs(x):
            colors[x] = 1
            for y in g[x]:
                if colors[y] == 1:
                    return True
                if colors[y] == 0 and dfs(y):
                    return True
            colors[x] = 2
            return False
        
        for i in range(numCourses):
            if colors[i] == 0 and dfs(i):
                return False
        return True
        