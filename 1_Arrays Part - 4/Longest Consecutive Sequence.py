from typing import List
'''
Naive Approach (Brute Force): O(n^2)
Time: O(n²)
Idea: For each number, check how long the sequence continues.
'''
# def longestConsecutive(nums: List[int]) -> int:
#     longest = 0

#     for num in nums:
#         current = num
#         count = 1

#         while current + 1 in nums:
#             current += 1
#             count += 1

#         longest = max(longest, count)

#     return longest

'''
Better Approach (Sorting): O(nlogn)
Sorting takes O(n log n).
Still a valid solution for interviews unless O(n) is explicitly required.
'''
# def longestConsecutive(nums: List[int]) -> int:
#     if not nums:
#         return 0

#     nums.sort()
#     longest = 1
#     count = 1

#     for i in range(1, len(nums)):
#         if nums[i] == nums[i - 1]:
#             continue  # Skip duplicates
#         elif nums[i] == nums[i - 1] + 1:
#             count += 1
#         else:
#             longest = max(longest, count)
#             count = 1

#     return max(longest, count)

'''
Optimal Approach (Using Set): O(n)
We only start a sequence when num - 1 is not in the set.
This prevents duplicate counting and ensures O(n) time.
'''
def longestConsecutive(nums: List[int]) -> int:
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:  # Only start counting if it's the beginning of a sequence
            current = num # assign only when 
            count = 1

            # main loop for checking
            while current + 1 in num_set:
                current += 1
                count += 1

            longest = max(longest, count)

    return longest

'''
Sequence Start	Counted Sequence	Length
1	            1, 2, 3, 4	        4
100	            100	                1
200	            200	                1

# Choose the max len among the lengths each time
'''

nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))
