class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change_bank = {5: 0, 10: 0, 20: 0}
        if bills[0] == 10 or bills[0] == 20:
            return False

        for b in bills:
            if b == 5:
                change_bank[5] += 1
            elif b == 10:
                if change_bank[5] == 0:
                    return False
                change_bank[5] -= 1
                change_bank[10] += 1
            elif b == 20:
                remain = 15
                if change_bank[10] != 0:
                    remain -= 10
                    change_bank[10] -= 1
                num = remain / 5
                if change_bank[5] < num:
                    return False
                change_bank[5] -= num
        return True