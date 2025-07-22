'''
Given an array of integers nums and an integer k, return the total number of subarrays whose XOR equals to k.
'''
'''
Brute Force (O(n³))
Approach:
Generate all subarrays
For each subarray, calculate the XOR
Count if XOR == k
'''
# def subarraysWithXorK(nums, k):
#     n = len(nums)
#     count = 0

#     for i in range(n):
#         for j in range(i, n):
#             xor_sum = 0
#             for m in range(i, j + 1):
#                 xor_sum ^= nums[m]
#             if xor_sum == k:
#                 count += 1
#     return count

'''
Better Approach (O(n²))
Approach:
Fix the start of the subarray i
Iterate from i to n-1, maintaining cumulative XOR
If at any point XOR == k, count it
'''
# def count_subarrays_better(nums, k):
#     n = len(nums)
#     count = 0

#     for i in range(n):
#         xor_sum = 0
#         for j in range(i, n):
#             xor_sum ^= nums[j]
#             if xor_sum == k:
#                 count += 1
#     return count
        
'''
Optimal Approach (O(n)) → "Prefix" XOR + HashMap
Iterate through nums and compute running XOR
For each prefix_xor, check if (prefix_xor ^ k) exists in hashmap
Add its frequency to the count
Store/update prefix_xor in the hashmap
'''
def subarraysWithXorK(nums, k):
    count = 0

    prefix_xor = 0
    prefix_map = {0: 1}

    for num in nums:
        prefix_xor ^= num

        target = prefix_xor ^ k

        count += prefix_map.get(target, 0)

        prefix_map[prefix_xor] = prefix_map.get(prefix_xor, 0) + 1

    return count

nums =  [4, 2, 2, 6, 4]
k = 6
print(subarraysWithXorK(nums, k))