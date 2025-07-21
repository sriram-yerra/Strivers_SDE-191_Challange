'''
Boyer-Moore Voting Algorithm (Optimal)
'''
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        count1 = count2 = 0
        candidate1 = candidate2 = None

        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        result = []
        n = len(nums)
        if nums.count(candidate1) > n // 3:
            result.append(candidate1)
        if candidate2 != candidate1 and nums.count(candidate2) > n // 3:
            result.append(candidate2)

        return result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3,2,3]))        
    print(sol.majorityElement([1,1,1,3,3,2,2]))  

