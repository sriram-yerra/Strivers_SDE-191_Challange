'''Why Cycle Detection: Floyd's Cycle Detection?

We treat the array as a linked list:
Treat i as a node
Treat nums[i] as a pointer to next node
Since numbers are between 1 and n, and we have n+1 values, there must be a cycle.
Just like finding the start of a loop in a linked list — we’ll use the Tortoise and Hare Algorithm.
'''
# class Solution:
#     def findDuplicate(self, nums):
#         # Phase 1: Detect cycle
#         slow = nums[0]
#         fast = nums[0]

#         while True:
#             slow = nums[slow]
#             fast = nums[nums[fast]]
#             if slow == fast:
#                 break

#         # Phase 2: Find the entrance to the cycle
#         fast = nums[0]
#         while slow != fast:
#             slow = nums[slow]
#             fast = nums[fast]

#         return slow

class Solution:
    def findDuplicate(self, nums):
        low_val, high_val = 1, len(nums) - 1
        while low_val < high_val:
            mid = (low_val + high_val) // 2
            
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1

            if count > mid:
                high_val = mid  # duplicate is in [low, mid]
            elif count <= mid:
                low_val = mid + 1  # duplicate is in [mid+1, high]

        return low_val

if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 3, 4, 2, 2]
    print(sol.findDuplicate(nums1))