class Solution:
    def isValid(self, w1, w2):
        count = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                count += 1
        return count == 1
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        # breadth first search
        q = deque()
        not_visited = set(wordList)
        for w in wordList:
            if self.isValid(beginWord, w):
                q.append(w)
                not_visited.remove(w)
        count = 1
        while q:
            count += 1
            q_len = len(q)
            for _ in range(q_len):
                word = q.popleft()
                if word == endWord:
                    return count
                for nxt in list(not_visited):
                    if self.isValid(word, nxt):
                        q.append(nxt)
                        not_visited.remove(nxt)
        return 0
                
