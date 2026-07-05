class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if not stack and not star:
                    return False
                if stack:
                    stack.pop()
                else:
                    star.pop()
            else:
                star.append(i)
        while stack:
            lastl = stack.pop()
            if not star:
                return False
            lastr = star.pop()
            if lastl > lastr:
                return False
        return True