# trabsform into 1D Array, then binary search

from typing import List
import math

def src(mat : List[List[int]], tar: int) -> int:
    m = len(mat)
    n = len(mat[0])

    temp = []
    for i in range(0, m):
        for j in range(0, n):
            temp.append(mat[i][j]) 

    left = 0
    right = len(temp) - 1

    while left <= right:
        mid = math.floor(left + (right-left)/2)
        if temp[mid] == tar:
            return mid
        elif temp[mid] > tar :
            right = mid - 1
        elif temp[mid] < tar :
            left = mid + 1

    return 

if __name__ == "__main__":
    a = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    tar = 8
    
    res = src(a, tar)
    print(res)