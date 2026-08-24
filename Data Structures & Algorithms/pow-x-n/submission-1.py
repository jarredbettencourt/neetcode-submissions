class Solution:
    def myPow(self, x: float, n: int) -> float:
        # count = 1
        # for _ in range(abs(n), 0, -1):
        #     count *= x
        # return 1 / count if n < 0 else count 
        
        
        # if count == 0:
        #     return 1
        # # Account for positive n
        
        # m = abs(n)
        # power_array = [-1 for _ in range(n)] 
        # while m > 0:


        
        
        # if n % 2 == 1:
        #     return count * x 
        # return count * x

        def myPowRecursive(x, n, power_map):
            if n == 0:
                return 1
            if n in power_map:
                return power_map[n]


            power_map[n] = x * myPowRecursive(x, n-1, power_map)
        
            return power_map[n]

        m = abs(n)
        square = myPowRecursive(x, m, {})
        return square if n > 0 else 1 / square
