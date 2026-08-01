class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def add_word(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.isWord = True
    
class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()
        for word in words:
            root.add_word(word)
        
        m, n = len(board), len(board[0])
        res = set()


        def dfs(i, j, node, word):
            if (i < 0 or j < 0 or i >= m or j >= n or board[i][j] == "*" 
            or board[i][j] not in node.children):
                return
            c = board[i][j]
            board[i][j] = "*"
            nxt = node.children[c]
            word += c
            if nxt.isWord:
                res.add(word)
            dfs(i + 1, j, nxt, word)
            dfs(i - 1, j, nxt, word)
            dfs(i, j + 1, nxt, word)
            dfs(i, j - 1, nxt, word)
            board[i][j] = c
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, root, "")
        return list(res)


