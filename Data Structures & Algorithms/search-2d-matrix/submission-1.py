class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col1 = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            col1.append(matrix[i][0])

        l, r = 0, m - 1
        while l < r:
            mid = (l + r + 1) // 2
            if col1[mid] == target:
                return True
            elif col1[mid] > target:
                r = mid - 1
            else: 
                l = mid
        targetR = matrix[l]
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r + 1) // 2
            if targetR[mid] == target:
                return True
            elif targetR[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
