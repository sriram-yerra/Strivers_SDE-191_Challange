from typing import List
# we can sort to avoid the repeating triplets
'''
Approach-1: Brute Force
1. using for loops
'''
# def threeSum(nums: List[int]) -> List[List[int]]:
#     n = len(nums)
#     ll = set() # for making the lists unique
#     lt = [] # convert them back to lists

#     for i in range(0, n):
#         for j in range(i+1, n):
#             for k in range(j+1, n):
#                 if nums[i] + nums[j] + nums[k] == 0:
#                     # lt = (nums[i], nums[j], nums[k])
#                     l = tuple(sorted((nums[i], nums[j], nums[k])))
#                     ll.add(l)
    
#     for i in ll:
#         lt.append(list(i))
    
#     return lt
    
#     # return [list(triplet) for triplet in ll]

'''
Approach-2: Using set
'''
# def threeSum(nums: List[int]) -> List[List[int]]:
#     n = len(nums)
#     res = set() # set for storing the res lists

#     for i in range(0, n):
#         seen = set() # set for storing elements
#         for j in range(i+1, n):
#             third = -(nums[i] + nums[j])
#             if third in seen:
#                 res.add(tuple(sorted((nums[i], nums[j], third))))
#             else:
#                 seen.add(nums[j])

#     return [list(tup) for tup in res]

'''
Approach-3: Without extra space, with sorting
# for this, first sort the array and then follow the procedure
# It reduces the extra hashset and make it constant space
'''
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort() # sorts in-place, won't return

    n = len(nums)
    res = []

    for i in range(0, n):
        if i > 0 and (nums[i] == nums[i-1]):
            continue

        j = i + 1
        k = n - 1

        while j < k:
            three = nums[i] + nums[j] + nums[k]

            # four condiitons
            if three < 0:
                j += 1
            elif three > 0:
                k -= 1
            elif three == 0:
                res.append([nums[i], nums[j], nums[k]])
            
                while j < k and nums[j] == nums[j+1]: # to skip all of the duplicates
                    j += 1
                while j < k and nums[k] == nums[k-1]:
                    k -= 1

                j += 1
                k -= 1

    return res

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))