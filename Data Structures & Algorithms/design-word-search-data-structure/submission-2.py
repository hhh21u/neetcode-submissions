class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.head = Node()

    def addWord(self, word: str) -> None:
        start = self.head
        for c in word:
            if c not in start.children:
                start.children[c] = Node()
            start = start.children[c]
        start.isEnd = True
        return

    def sub_search(self, prev: Node, word: str): # start {a, b} .ay
        if len(word) == 0:
            return prev.isEnd
        c = word[0]
        if c == ".":
            for child, c_node in prev.children.items():
                if self.sub_search(c_node, word[1:]): return True
        else:
            if c not in prev.children:
                return False
            if self.sub_search(prev.children[c], word[1:]): return True
        return False

    def search(self, word: str) -> bool:
        start = self.head
        return self.sub_search(start, word)
        
