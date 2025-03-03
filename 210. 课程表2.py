class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 参考课程表1
        preMap = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            preMap[cur].append(pre)
        visited = [0] * numCourses
        ans = []

        def dfs(x):
            visited[x] = 1
            for y in preMap[x]:
                if visited[y] == 1:
                    return True
                if visited[y] ==0 and dfs(y):
                    return True
            visited[x] = 2
            ans.append(x)
            return False
        
        for i in range(numCourses):
            if visited[i] ==0 and dfs(i):
                return []
        return ans
# 本题是课程表1的变种，只需要将课程表1中的返回值改为ans即可