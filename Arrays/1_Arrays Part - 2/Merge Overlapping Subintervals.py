class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        # Step 1: Sort intervals based on start time
        intervals.sort(key=lambda x: x[0])

        merged = []

        for i in intervals:
            # if merged is empty or no "overlap", add interval
            if not merged or merged[-1][1] < i[0]:
                merged.append(i)
            else:
                # overlap found, merge it
                merged[-1][1] = max(merged[-1][1], i[1])

        return merged

# Example usage
if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(sol.merge(intervals))  # Output: [[1,6],[8,10],[15,18]]