class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        leftset = set(["(", "{", "["])
        ma = {")": "(", "}": "{", "]": "["}
        for c in s: 
            if c in leftset:
                stack.append(c)
                continue
            if stack and ma[c] == stack[-1]:
                stack.pop()
            else:
                return False
        return True if len(stack) == 0 else False