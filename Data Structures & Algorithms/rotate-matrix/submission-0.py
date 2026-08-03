class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        l, r = 0, n - 1

        while l < r:
            top, bottom = l, r
            for i in range(r - l):
                # save top left
                top_left = matrix[top][l + i]
                matrix[top][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = top_left
            l += 1
            r -= 1
        
