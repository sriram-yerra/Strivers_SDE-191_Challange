# trabsform into 1D Array, then binary search

from typing import List
import math

def src(mat : List[int], tar: int) -> int:

    left = 0
    right = len(a) - 1

    while left <= right:
        mid = math.floor(left + (right-left)/2)
        if a[mid] == tar:
            return mid
        elif a[mid] > tar :
            right = mid - 1
        elif a[mid] < tar :
            left = mid + 1

    return 

if __name__ == "__main__":
    a = [1, 2, 3, 4]
    tar = 2
    
    res = src(a, tar)
    print(res)