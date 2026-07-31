class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(sub):
            l, r = 0, len(sub) - 1
            while l < r:
                if sub[l] != sub[r]:
                    return False
                l += 1
                r -= 1
            return True
        res = []
        def bt(idx, path):
            if idx == len(s):
                res.append(path.copy())
                return
            for i in range(idx + 1, len(s) + 1):
                if isPalindrome(s[idx:i]):
                    path.append(s[idx:i])
                    bt(i, path)
                    path.pop()
        bt(0, [])
        return res


        