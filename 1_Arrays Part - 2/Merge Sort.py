from typing import List
import math

# def merge(arr: List[int], low: int, mid: int, high: int) -> List[int]:
def merge(arr: List[int], low: int, mid: int, high: int) -> None:

    temp = []
    left = low # it is the first index of the left array
    right = mid + 1 # it is the first index for the right array

    while(left <= mid and right <= high):
        if (arr[left] <= arr[right]):
            temp.append(arr[left])
            left += 1

        # elif (arr[left] > arr[right]):
        else:
            temp.append(arr[right])
            right += 1

    # if elements in the arrays still lef after the comparions
    while (left <= mid):
        temp.append(arr[left])
        left += 1

    while (right <= high):
        temp.append(arr[right])
        right += 1

    # transfoer form temp to arr
    # for i in temp:
    #     arr.append(i)

    # for i in range(len(temp)):
    #     arr[i] = temp[i] 

    for i in range(low, high+1): # *************** IMP ************** #
        arr[i] = temp[i - low] 

    # return arr
    

def mergeSort(arr: List[int], low: int, high: int) -> List[int]:
# def mergeSort(arr: int, low: int, high: int) -> None:

    if low >= high:
        # return arr
        return 
    
    mid = math.floor(low + (high - low)/2)
    # mid = math.floor((low + high) / 2)

    mergeSort(arr, low, mid)
    mergeSort(arr, mid+1, high)
    merge(arr, low, mid, high)
    
    return arr

if __name__ == "__main__":
    arr = [1, 3, 2, 7, 6, 5, 4]
    low = 0
    n = len(arr)
    high = n - 1
    res = mergeSort(arr, low, high)
    print(res)