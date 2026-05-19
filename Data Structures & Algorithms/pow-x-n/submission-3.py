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

        def myPowRecursive(x, n):
            if n == 0:
                return 1
            
            res = myPowRecursive(x, n // 2)
            res *= res
            
            return res if n % 2 == 0 else x * res

        m = abs(n)
        res = myPowRecursive(x, m)
        # if m % 2 == 1: res = x * res
        return res if n >= 0 else 1 / res 
