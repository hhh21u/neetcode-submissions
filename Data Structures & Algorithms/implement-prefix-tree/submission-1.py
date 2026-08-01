class Node:
    def __init__(self, val):
        self.val = val
        self.children = {} # val to node
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.head = Node(0)

    def insert(self, word: str) -> None:
        start = self.head
        for i in range(len(word)):
            c = word[i]
            if c not in start.children:
                node = Node(c)
                start.children[c] = node
            
            node = start.children[c]
            start = node
        start.isEnd = True
        return 


    def search(self, word: str) -> bool:
        start = self.head
        for c in word:
            if c not in start.children:
                return False
            start = start.children[c]
        if start.isEnd:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        start = self.head
        for c in prefix:
            if c not in start.children:
                return False
            start = start.children[c]
        return True
        
        