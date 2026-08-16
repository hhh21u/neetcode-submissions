class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # bfs
        c2i = defaultdict(int)
        for i, c in enumerate(order):
            c2i[c] = i

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for i1, c1 in enumerate(w1):
                if i1 >= len(w2):
                    return False
                c2 = w2[i1]
                print(f"{c1}, {c2}")
                if c2i[c1] > c2i[c2]:
                    return False
                elif c2i[c1] < c2i[c2]:
                    break
        return True




