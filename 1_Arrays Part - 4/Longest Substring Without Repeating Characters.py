'''
Brute Force (O(n³))
Try every possible substring, check if it has all unique characters.
'''
# def lengthOfLongestSubstring(s: str) -> int:
#     n = len(s)
#     max_len = 0

#     for i in range(n):
#         for j in range(i, n):
#             substring = s[i:j+1]
#             if len(set(substring)) == len(substring):  # all unique
#                 max_len = max(max_len, j - i + 1)

#     return max_len

'''
Better Approach (O(n²)):
Use a set and try to expand the window as long as characters are unique.
'''
# def lengthOfLongestSubstring(s: str) -> int:
#     maxlen = 0
#     n = len(s)

#     for i in range(0, n):
#         seen = set()
#         for j in range(i, n):
#             if s[j] in seen:
#                 break
#             elif s[j] not in seen:
#                 seen.add(s[j])
            
#             maxlen = max(maxlen, j-i+1)

#     return maxlen

'''
Optimal with Dictionary (Track last index of each character)
'''
def lengthOfLongestSubstring(s):
    last_seen = {}
    left = 0
    right = 0
    max_len = 0

    for right in range(len(s)):
        char = s[right]

        # if char in last_seen:
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1  # jump past the last duplicate
        last_seen[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len


s = "abcabcbb"
print(lengthOfLongestSubstring(s))