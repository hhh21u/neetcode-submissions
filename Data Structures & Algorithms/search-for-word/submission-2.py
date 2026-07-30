class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) == 0: return True
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m, n = len(board), len(board[0])
        # visited = set()
        def dfs(x, y, idx):
            # print(f"enter {x}, {y}, {visited}")
            if idx == len(word):
                return True
            res = False
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if (nx < 0 
                or ny < 0 
                or nx >= m 
                or ny >= n 
                or (nx, ny) in visited or board[nx][ny] != word[idx]):
                    continue
                visited.add((nx, ny))
                res = res or dfs(nx, ny, idx + 1)
                visited.discard((nx, ny))
            return res
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add((i, j))
                    if dfs(i, j, 1):
                        return True
        return False
                
