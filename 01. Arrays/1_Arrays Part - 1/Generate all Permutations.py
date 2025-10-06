from typing import List
class Solution:
    # We follow recursion here
    # For recursion, Base case is very much important.

    # RECURSIVE APPROACH - 1: WITH EXTRA AUXILLARY SPACE
    # def recPerm(nums: List[int], used: List[bool], res: List[list[int]]) -> List[list[int]]:
    #     # base case:
    #     if len(nums) == 

    # RECURSIVE APPROACH - 1: WITHOUT EXTRA AUXILLARY SPACE
    def recPerm(self, nums: List[int], start: int, res: List[list[int]]) -> List[list[int]]:
        # start is a pointer which says to start the swapping, if it reaches end the -> stop
        if start == len(nums):
            res.append(nums[:]) # nums[:] -> for a shallow copy of the nums, but not nums directly

        for i in range(start, len(nums)):
            # swap to make each element as starting ele
            nums[start], nums[i] = nums[i], nums[start]

            self.recPerm(nums, start+1, res)

            # BackTrack --> Undo Swap
            nums[start], nums[i] = nums[i], nums[start]            

        return res

    def permutate(self, nums: List[int]) -> None:
        res = []
        start = 0
        perm = self.recPerm(nums, start, res)
        # for i in perm:
        #     print(i)
        return res

'''
For using INBUILD functions:

from itertools import permutations
ele = [1,2,3]
all_perm = list(permutations(elements))

for perm in all_perm:
    print(perm)
'''

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3]
    perms = sol.permutate(nums)
    for p in perms:
        print(p)  

