class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        def simulate(i):
            arr_len = len(gas)
            cur_gas = gas[i]
            start_idx = i
            while cur_gas >= cost[i]:
                cur_gas -= cost[i]
                i = (i + 1) % arr_len
                if i == start_idx:
                    return True
                cur_gas += gas[i]
            return False

        for i in range(len(gas)):
            if simulate(i): return i
        return -1
                
        
