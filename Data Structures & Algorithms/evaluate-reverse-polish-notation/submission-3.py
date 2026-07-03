class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = len(tokens)
        res = 0
        for c in tokens:
            if c not in set(["+", "*", "-", "/"]):
                stack.append(int(c))
                continue
            print(stack, res)
            right = stack.pop()
            left = stack.pop()
            if c == "+":
                res = left + right
            elif c == "-":
                res = left - right
            elif c == "*":
                res = left * right
            elif c =="/":
                res = int(left / right)
            stack.append(res)
        return res if len(stack) == 0 else int(stack[0])
