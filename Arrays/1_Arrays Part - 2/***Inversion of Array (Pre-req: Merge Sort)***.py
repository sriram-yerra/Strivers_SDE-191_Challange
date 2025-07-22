'''
Notes:
1. consider an algorithm where, there are 2 arrays which are sorted
2. for finding the pairs which satisfy the condition if i<j & nums[i] > nums[j].
3. we will compare the elements by having 2 pointers at the starng of each of the arrays.
4. if ele1 in the arr1 is > ele1 in the arr2, the elements after that ele1 in arr1 are always > ele1 in arr2.
5. So, no need to iterate for the remaining in arr1 if we found this logic.
6. we need to move both the pointers according to the logic.

*. The above step can be used at the intermediate step of the merge-sort for counting: we use this while merging
'''

from typing import List
import math

def merge(arr : List[int], low : int, mid : int, high : int) -> int:
    temp = []   # temporary array
    left = low  # starting index of left half of arr
    right = mid + 1 # starting index of right half of arr

    cnt = 0     

    # storing elements in the temporary array in a sorted manner
    while (left <= mid and right <= high):
        if (arr[left] <= arr[right]):
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            cnt += (mid - left + 1)  # counting happens here # Imp
            right += 1

    while (left <= mid):
        temp.append(arr[left])
        left += 1

    while (right <= high):
        temp.append(arr[right])
        right += 1

    # transfering all elements from temporary to arr
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

    return cnt   

def mergeSort(arr : List[int], low : int, high : int) -> int:
    cnt = 0
    if low >= high:
        return cnt
    mid = math.floor((low + high) / 2)
    cnt += mergeSort(arr, low, mid)    # left half
    cnt += mergeSort(arr, mid + 1, high)  # right half
    cnt += merge(arr, low, mid, high)  # merging sorted halves
    print(arr)
    return cnt
    
def numberOfInversions(a : List[int], n : int) -> int:
    n = len(a)
    return mergeSort(a, 0, n - 1) # returns the number of pairs

if __name__ == "__main__":
    a = [5, 4, 3, 2, 1]
    n = 5
    cnt = numberOfInversions(a, n)
    print(cnt)