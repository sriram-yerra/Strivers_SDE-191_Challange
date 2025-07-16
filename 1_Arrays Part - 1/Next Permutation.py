from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        k = -1

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                k = i
                break

        # base condition
        if k == -1:
            nums.reverse()
            return

        temp = nums[k+1:] # temp from k+1 to end and sort it
        temp.sort()

        # Find the smallest element in temp > nums[k]
        for i in range(len(temp)):
            if temp[i] > nums[k]:
                # Swap
                nums[k], temp[i] = temp[i], nums[k]
                break

        nums[k+1:] = temp

        return nums

if __name__ == "__main__":
    sol = Solution()

    nums = [1,2,3,5,4]
    res = sol.nextPermutation(nums)

    print(res)