from typing import List

# BRUTE FORCE: --> USING MERGE SORT

# BETTER: --> USING COUTER

# OPTIMAL: --> USING "DUTCH NATIONAL FLAG ALGORITHM"
'''
Use 3 Pointers
[from 0.....to (low-1)] -> contains 0
[from 0.....to (low-1)] -> contains 1
[from 0.....to (low-1)] -> contains 2

[(0)...(low-1)] [(low)...(mid-1)] "[(mid)...(high)]" [(hight+1)...(n-1)]
OUR ARRAY IS --> "[(mid)...(high)]"
''' 

class Solution:
    def swap(self, nums: List[int], i: int, j: int) -> None:
        nums[i], nums[j] = nums[j], nums[i]

    def sortColors(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        mid = 0
        high = n-1
        while mid <= high:
            if nums[mid] == 0:
                self.swap(nums, mid, low)
                low += 1
                mid += 1
            
            elif nums[mid] == 1:
                mid += 1

            elif nums[mid] == 2:
                self.swap(nums, mid, high)
                high -= 1

        return nums

if __name__ == "__main__":
    sol = Solution()

    # nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums = [2,0,2,1,1,0]

    res = sol.sortColors(nums)

    print(res)