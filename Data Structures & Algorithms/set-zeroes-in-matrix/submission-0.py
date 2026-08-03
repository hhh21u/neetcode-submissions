class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        zeros = []
        emptyR = set()
        emptyC = set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    emptyR.add(i)
                    emptyC.add(j)
        
        for i in range(m):
            for j in range(n):
                if i in emptyR or j in emptyC:
                    matrix[i][j] = 0
        
        
