'''
Approach-1: Recursion, all the paths should be tried with recursion.
            Make a recursive approach from first to last.
            Base case: if i >= n or j >= n
'''
# from functools import lru_cache
# @lru_cache(maxsize = None)
# def unqpaths(m, n, i, j):
    # if i == m-1 and j == n-1:
    #     return 1 # every time it reaches end, count increases
    # if i >= m or j >= n:
    #     return 0
#     return unqpaths(m, n, i+1, j) + unqpaths(m, n, i, j+1)

# def uniquePaths(m: int, n: int) -> int:
#     @lru_cache(maxsize=None)
#     def count_paths(i, j):
#         if i == m - 1 and j == n - 1:
#             return 1  # Reached destination
#         if i >= m or j >= n:
#             return 0  # Out of bounds
#         return count_paths(i + 1, j) + count_paths(i, j + 1)S
#     return count_paths(0, 0)

'''
Approach-2: Dynamic Programming -> reduces the overlappping subProblems.
            We are using Memoization.
'''
def unqpaths(m, n, i, j, dp):
    # create a matrix for dp
    # dp = []
    # for i in range(m):
    #     dp.append([1]*n)
    # dp = [[-1]*n for _ in range(m)]

    if i == m-1 and j == n-1:
        return 1 # every time it reaches end, count increases
    if i >= m or j >= n:
        return 0
    
    if dp[i][j] != -1:
        return dp[i][j]
    elif dp[i][j] == -1:
        dp[i][j] = unqpaths(m, n, i+1, j, dp) + unqpaths(m, n, i, j+1, dp)

    return dp[i][j]

if __name__ == "__main__":
    m, n = 2, 3
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    print(unqpaths(m, n, 0, 0, dp)) 

'''
Approach-3: Optimal Space Approach
'''
# def unqpaths(m: int, n: int) -> int:
#     dp = [1] * n # number of columns or size of the row

#     for i in range(1, m):
#         for j in range(1, n):
#             dp[j] += dp[j - 1]
#     return dp[-1] # [1,2,3] for m,n = 2,3

'''
Approach-4: Combinatorics Formula -> Most Optimal
'''
# import math
# def unqpaths(m: int, n: int) -> int:
#     return math.comb(m + n - 2, n - 1)

if __name__ == "__main__":
    m, n = 3, 7
    print(unqpaths(m, n, 0, 0))
    # print(unqpaths(m, n))

