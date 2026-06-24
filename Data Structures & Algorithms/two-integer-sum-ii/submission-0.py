class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1 3 4 8 9
        left, right = 0, len(numbers) - 1
        while left < right: 
            if numbers[left] + numbers[right] == target: 
                return [left + 1, right + 1]
            if numbers[left] + numbers[right] < target: 
                left += 1
            else:
                right -= 1
        return None