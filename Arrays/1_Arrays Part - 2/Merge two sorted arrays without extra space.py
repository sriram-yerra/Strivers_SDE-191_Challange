'''
Brute-Force: Swapping & Sorting Approach

Loop through nums1's first m elements.
If any nums1[i] > nums2[0]:
Swap nums1[i] and nums2[0]
Re-sort nums2 to keep it in order.
Finally, copy all of nums2 to the back of nums1.
'''
class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1  # pointer at end of valid nums1
        j = n - 1  # pointer at end of nums2
        k = m + n - 1  # pointer at end of nums1 (full size)

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If nums2 is still not empty
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1