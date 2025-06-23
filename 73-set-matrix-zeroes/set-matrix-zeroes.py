class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        pnts = []
        m = len(matrix[0])
        n = len(matrix)
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    pnts.append((i,j))
                    
        for i,j in pnts:
            for k in range(n):
                #print(k,j)
                if matrix[k][j] == 0:
                    continue
                matrix[k][j] = -11
            for k in range(m):
                #print(i,k)
                if matrix[i][k] == 0:
                    continue
                matrix[i][k] = -11 
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == -11:
                    matrix[i][j] = 0
                    
        
                