# Given an integer array nums of size n containing values from [1, n] and each value appears exactly once in the array, except for A, which appears twice and B which is missing.
# Return the values A and B, as an array of size 2, where A appears in the 0-th index and B in the 1st index.
class Solution:
    def findMissingRepeatingNumbers(self, nums):
        n = len(nums)
        S = n * (n + 1) // 2
        S2 = n * (n + 1) * (2 * n + 1) // 6

        sum_nums = sum(nums)
        sum_sq_nums = sum(x * x for x in nums)

        diff = sum_nums - S             # A - B
        sq_diff = sum_sq_nums - S2      # A^2 - B^2

        # A + B = sq_diff / diff
        sum_ab = sq_diff // diff

        A = (diff + sum_ab) // 2
        B = A - diff

        return [A, B]


if __name__ == "__main__":
    sol = Solution()
    nums1 = [3, 5, 4, 1, 1]
    print(sol.findMissingRepeatingNumbers(nums1))