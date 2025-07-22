'''
Optimal Approach:
Insted of looking for the sum k in the middle, look fir prefixsum-k from beginning.
Simialr logic as 2 sum, where it looks for target-val2 = val1

Store every prefix sum in the dict
If the current_prefix_sum-k in the dict, then it is a valid subarray 
'''
def countSubarraysWithSumK(nums, k):
    prefix_sum = 0
    count = 0
    prefix_map = {0: 1}  # prefix_sum 0 occurs once initially

    for num in nums:
        prefix_sum += num
        target = prefix_sum - k

        # Incrementing count each time, if there then inc with that val, else returns 0, i.2 count remains unchanged.
        count += prefix_map.get(target, 0)

        # Incrementing the val if same prefix sum arrives again or create new one by making its value to 1.
        # Record that prefix_sum has occurred once more.
        # If this prefix sum is new, it initializes to 1
        # If it's already seen, increment its count by 1
        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

    return count

# Test
nums = [10, 5, 2, 7, 1, 9]
k = 15
print(countSubarraysWithSumK(nums, k))  # Output: 3
