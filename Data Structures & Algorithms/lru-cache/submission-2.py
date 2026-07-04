class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.cacheTable = {}
        self.root = self.Node(0, 0)
        self.end = self.root
        self.capacity = capacity

    def deleteNode(self, node):
        node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.end = node.prev
    
    def appendNode(self, node):
        node.prev = self.end
        self.end.next = node
        self.end = self.end.next
        node.next = None
        

    def get(self, key: int) -> int:
        if key not in self.cacheTable:
            return -1
        curNode = self.cacheTable[key]
        self.deleteNode(curNode)
        self.appendNode(curNode)
        print(f"check {key}, {curNode}, {self.root.next}")
        return curNode.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cacheTable:
            cur = self.cacheTable[key]
            cur.val = value
            self.deleteNode(cur)
            self.appendNode(cur)
        else:
            newNode = self.Node(key, value)
            self.cacheTable[key] = newNode
            self.appendNode(newNode)
            if len(self.cacheTable) > self.capacity:
                print(self.cacheTable)
                pop = self.root.next
                self.deleteNode(pop)
                del self.cacheTable[pop.key]






        
