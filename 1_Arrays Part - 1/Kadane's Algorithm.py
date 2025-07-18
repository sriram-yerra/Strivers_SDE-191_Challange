from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        # if n == 0: 
        #     return

        if not nums:
            return 0

        currsum = maxsum = nums[0]

        for i in range(1, n):
            currsum = max(nums[i], currsum + nums[i])
            maxsum = max(currsum, maxsum)

        return maxsum

if __name__ == "__main__":
    sol = Solution()

    # nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums = []

    res = sol.maxSubArray(nums)

    print(res)