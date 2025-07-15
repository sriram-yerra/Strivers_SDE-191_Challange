from typing import List

class Solution:

    def isFirstRowZero(self, mat: List[List[int]], n: int) -> bool:
        for j in range(n):
            if mat[0][j] == 0:
                return True  

    def isFirstColZero(self, mat: List[List[int]], m: int) -> bool:
        for i in range(m):
            if mat[i][0] == 0:
                return True
            
    def setZeroes(self, mat: List[List[int]]) -> None:
        if not mat:
            return 
        
        m = len(mat)
        n = len(mat[0])

        first_row_zero = self.isFirstRowZero(mat, n)
        first_col_zero = self.isFirstColZero(mat, m)

        # using first row and column as markers # Making Phase
        for i in range(1, m):
            for j in range(1, n):
                if mat[i][j] == 0:
                    mat[i][0] = 0
                    mat[0][j] = 0

        # set cells 0 based on markers # Applying phase
        for i in range(1, m):
            for j in range(1, n):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0

        if first_row_zero:
            for j in range(m):
                mat[0][j] = 0

        if first_col_zero:
            for i in range(n):
                mat [i][0] = 0
            

if __name__ == "__main__":
    sol = Solution()
    mat = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 8, 9]
    ]
    print("Before:")
    for row in mat:
        print(row)

    sol.setZeroes(mat)

    print("\nAfter:")
    for row in mat:
        print(row)
