class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 有效的数独
        row = [[0]*9 for _ in range(9)]
        col = [[0]*9 for _ in range(9)]
        block = [[0]*9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j]) - 1#num 是索引
                    b = (i//3)*3 + j//3#根据行列的关系确定块
                    # 通过 (i // 3) * 3，我们将行块编号转换为块的基准编号（0, 3, 6）。 通过 + (j // 3)，我们将列块编号加到基准编号上，得到最终的块编号
                    if row[i][num] or col[j][num] or block[b][num]:
                        return False
                    row[i][num] = col[j][num] = block[b][num] = 1
        return True


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 螺旋矩阵
        if not matrix:
            return []
        l,r,t,b,res = 0,len(matrix[0])-1,0,len(matrix)-1,[]
        while True:
            for i in range(l,r+1):
                res.append(matrix[t][i])
            t+=1
            if t>b:
                break
            for i in range(t,b+1):
                res.append(matrix[i][r])
            r-=1
            if r<l:
                break
            for i in range(r,l-1,-1):
                res.append(matrix[b][i])
            b-=1
            if b<t:
                break
            for i in range(b,t-1,-1):
                res.append(matrix[i][l])
            l+=1
            if l>r:
                break
        return res                   

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        