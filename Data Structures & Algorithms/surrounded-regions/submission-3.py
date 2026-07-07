class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        def dfs(i, j):
            board[i][j] = "S"
            visited.add((i, j))
            for dx, dy in dirs:
                nx, ny = i + dx, j + dy
                if nx < 0 or ny < 0 or nx >= m or ny >= n or (nx, ny) in visited or board[nx][ny] == "X":
                    continue
                dfs(nx, ny)
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    if (i, j) not in visited and board[i][j] == "O":
                        dfs(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "S":
                    board[i][j] = "O"        