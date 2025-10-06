from typing import List
import math

class Solution:
    def myPow(self, x: float, n: int) -> float:

        # return math.pow(x, n)
    
        def fast_pow(base, power):
            # Base case here
            if power == 0:
                return 1.0
            
            # if power != 0
            half = fast_pow(base, power // 2)
            # if even
            if power % 2 == 0:
                return half * half
            # elif odd
            else:
                return half * half * base
        
        # Handle negative cases also
        if n < 0:
            x = 1 / x
            n = -n

        return fast_pow(x, n)


if __name__ == "__main__":
    x = 2.00000
    n = 10

    sol = Solution()

    res = sol.myPow(x, n)
    print(res)