'''
We can solve this using the Merge Sort while merging the array parts.
'''
from typing import List
import math

class Solution:
    def merge(self, arr : List[int], low : int, mid : int, high : int) -> int:
        temp = []   # temporary array

        cnt = 0     
        right = mid + 1
        for i in range(low, mid + 1):
            while right <= high and arr[i] > 2 * arr[right]: # Condition
                right += 1
            cnt += (right - (mid + 1))

        left = low  # starting index of left half of arr
        right = mid + 1 # starting index of right half of arr

        # storing elements in the temporary array in a sorted manner
        while (left <= mid and right <= high):
            if (arr[left] <= arr[right]):
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                # if arr[left] > 2*(arr[right]):
                #     cnt += (mid - (left + 1))  # counting happens here # Imp
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

    def mergeSort(self, arr : List[int], low : int, high : int) -> int:
        cnt = 0
        if low >= high:
            return cnt
        mid = math.floor((low + high) / 2)
        cnt += self.mergeSort(arr, low, mid)    # left half
        cnt += self.mergeSort(arr, mid + 1, high)  # right half
        cnt += self.merge(arr, low, mid, high)  # merging sorted halves
        # print(arr)
        return cnt

    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        return self.mergeSort(nums, 0, n - 1) # returns the number of pairs
    
if __name__ == "__main__":
    a = [1,3,2,3,1]
    sol = Solution()
    cnt = sol.reversePairs(a)
    print(cnt)