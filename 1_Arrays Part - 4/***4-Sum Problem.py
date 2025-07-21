'''
Approach-1: Brute Force
Time Comp: n^4
'''
# from typing import List

# def fourSum(nums: List[int], target: int) -> List[List[int]]:
#     n = len(nums)
#     result = set()  # to avoid duplicates

#     for i in range(n):
#         for j in range(i + 1, n):
#             for k in range(j + 1, n):
#                 for l in range(k + 1, n):
#                     total = nums[i] + nums[j] + nums[k] + nums[l]
#                     if total == target:
#                         quad = tuple(sorted([nums[i], nums[j], nums[k], nums[l]]))
#                         result.add(quad)  # use set to store unique quads

#     return [list(q) for q in result]

'''
Approach-2: Using set()
Time Comp: n^4
Here it takes the extra space of len "n"
'''
# from typing import List

# def fourSum(nums: List[int], target: int) -> List[List[int]]:
#     n = len(nums)
#     result = set()
#     nums.sort()  # Sorting helps avoid duplicates

#     for i in range(n):
#         for j in range(i + 1, n):
#             seen = set()
#             new_target = target - nums[i] - nums[j]

#             for k in range(j + 1, n):
#                 fourth = new_target - nums[k]
#                 if fourth in seen:
#                     quad = tuple(sorted([nums[i], nums[j], nums[k], fourth]))
#                     result.add(quad)
#                 seen.add(nums[k])
    
#     return [list(quad) for quad in result]

'''
Once listen to Strivers 4-Sum lecture
'''

'''
Approach-1: 2-Pointer Approach, with sorting without extra space
# for this, first sort the array and then follow the procedure
It reduces the extra hashset and make it constant space
'''
from typing import List

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort() # sorts in-place, won't return

    n = len(nums)
    res = []

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # below is the actual full code same loop for 3sum
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            k = j + 1
            l = n - 1

            while k < l:
                total = nums[i] + nums[j] + nums[k] + nums[l]

                # four condiitons
                if total < target:
                    k += 1
                elif total > target:
                    l -= 1
                elif total == target:
                    res.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1
                
                    while k < l and nums[k] == nums[k + 1]: # to skip all of the duplicates
                        k += 1
                    while k < l and nums[l] == nums[l - 1]:
                        l -= 1

    return [i for i in res]

if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    result = fourSum(nums, target)
    print(result)