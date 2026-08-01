class Node:
    def __init__(self):
        self.children = {}
    
class Solution:
    def search(self, start, word):
        for c in word:
            if c not in start.children:
                return False
            start = start.children[c]
        return True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        start = Node()
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m, n = len(board), len(board[0])

        def buildGraph(start, nx, ny, depth):
            if nx < 0 or ny < 0 or nx >=m or ny >= n or board[nx][ny] == "." or depth == 10:
                return
            c = board[nx][ny]
            board[nx][ny] = "."
            if c not in start.children:
                start.children[c] = Node()

            for dx, dy in dirs:
                i, j = nx + dx, ny + dy
                buildGraph(start.children[c], i, j, depth + 1)
            board[nx][ny] = c
        
        for i in range(m):
            for j in range(n):
                buildGraph(start, i, j, 0)
        res = []
        for word in words:
            if self.search(start, word):
                res.append(word)
        return res

