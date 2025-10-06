from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        res = []

        for i in range(numRows):
            res.append([])

        for i in range(0, numRows):
            res[i] = [0]*(i+1)

        res[0][0] = 1

        for i in range(1, numRows):
            k = len(res[i])
            res[i][0] = 1
            res[i][k-1] = 1

        for i in range(2, numRows):
            p = res[i-1]
            for j in range(len(res[i])):
                if res[i][j] == 0:
                    res[i][j] = res[i-1][j-1] + res[i-1][j]
        '''
        res = [[1]]  # First row

        for i in range(1, numRows):
            prev = res[-1]
            row = [1]  # First element
            for j in range(1, i):
                row.append(prev[j - 1] + prev[j])
            row.append(1)  # Last element
            res.append(row)
        '''

        return res
        

if __name__ == "__main__":
    sol = Solution()
    numRows = 1

    res = sol.generate(numRows)

    for row in res:
        print(row)    