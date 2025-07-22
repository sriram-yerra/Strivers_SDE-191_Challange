'''
Brute Force Approach — O(n³)
'''
# def longestSubarray(nums, k):
#     n = len(nums)
#     max_len = 0

#     for i in range(n):
#         for j in range(i, n):
#             current_sum = 0
#             for l in range(i, j + 1):
#                 current_sum += nums[l]
#             if current_sum == k:
#                 max_len = max(max_len, j - i + 1)

#     return max_len

'''
Slightly Better — O(n²)
'''
# def longestSubarray(nums, k):
#     n = len(nums)
#     max_len = 0

#     for i in range(n):
#         curr_sum = 0
#         for j in range(i, n):
#             curr_sum += nums[j]
#             if curr_sum == k:
#                 max_len = max(max_len, j-i+1)

#     return max_len

'''
Optimal Approach — O(n) using Prefix Sum + HashMap
'''
def longestSubarray(nums, k):
    n = len(nums)
    max_len = 0

    prefix_sum = 0
    # prefix_sum -> first_index
    prefix_map = {} # a dictonary

    for i, num in enumerate(nums):
        prefix_sum += num

        if prefix_sum == k:
            max_len = i + 1

        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i

        if prefix_sum - k in prefix_map:
            max_len = max(max_len, i - prefix_map[prefix_sum - k])

    return max_len

nums = [10, 5, 2, 7, 1, 9]
k = 15
print(longestSubarray(nums, k))