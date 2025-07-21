'''
 "Boyer-Moore" Majority Vote Algorithm:
1. Solve the problem in linear time and in O(1) space
2. Intuition:
    If you have a majority element (> n/2 times), it will outvote all others combined.
    The idea is like canceling out non-majority votes with the majority ones.
'''

from typing import List

def majorityElement(nums: List[int]) -> int:
    count = 0
    candidate = None

    for num in nums:
        # here for each element, when the new element arrives then count camcles out
        if count == 0:
            candidate = num
            
        if num == candidate:
            count += 1
        elif num != candidate:
            count -= 1

    return candidate

if __name__ == "__main__":
    a = [2, 2, 1, 1, 1, 2, 2]
    res = majorityElement(a)
    print(res)

'''
Counting dict from zero:
counts[num] = counts.get(num, 0) + 1
'''