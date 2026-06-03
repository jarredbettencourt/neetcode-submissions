class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # def simulate(i):
        #     arr_len = len(gas)
        #     cur_gas = gas[i]
        #     start_idx = i
        #     while cur_gas >= cost[i]:
        #         cur_gas -= cost[i]
        #         i = (i + 1) % arr_len
        #         if i == start_idx:
        #             return True
        #         cur_gas += gas[i]
        #     return False

        # for i in range(len(gas)):
        #     if simulate(i): return i
        # return -1
        if sum(gas) < sum(cost):
            return -1

        start_idx = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start_idx += 1
                tank = 0

        return start_idx + 1
