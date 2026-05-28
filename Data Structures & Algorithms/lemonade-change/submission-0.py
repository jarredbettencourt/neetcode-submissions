class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        change_pairing = {
            0: 5,
            1: 10,
            2: 20
        }

        bank = [0] * 3
        if bills[0] > 5:
            return False
        bank[0] = 1

        for i in range(1, len(bills)):
            cost = bills[i]
            if cost == 5:
                bank[0] += 1
            elif cost == 10:
                bank[1] += 1
            elif cost == 20:
                bank[2] += 1
            change = bills[i] - 5
            print(bank)
            for j in range(len(bank) - 1, -1, -1):
                while bank[j] > 0 and (change - change_pairing[j]) >= 0:
                    change -= change_pairing[j] 
                    bank[j] -= 1
            if change != 0:
                return False

        
                    
        return True