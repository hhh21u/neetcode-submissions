class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left <= right:
            while left < len(s) and not s[left].isalnum():
                left += 1
            while right >= 0 and not s[right].isalnum():
                right -= 1
            if left > len(s) - 1 or right < 0: break
            if s[left].lower() != s[right].lower():
                print(f"{s[left]}, right: {s[right]}")
                return False
            left += 1
            right -= 1
        return True