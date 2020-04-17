


'''
Contiguous Array
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
'''
class Solution1:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = 0
        index_map = dict()
        index_map[0] = -1
        res = 0        
        for i, num in enumerate(nums):
            if num == 0:
                total_sum -= 1
            else:
                total_sum += 1
            if total_sum in index_map:
                res = max(res, i - index_map[total_sum])
            else:
                index_map[total_sum] = i
        return res


import collections
class Solution2:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = [0] * len(nums)
        dmap = collections.defaultdict(int)
        last = 0
        for i, n in enumerate(nums):
            last += 2 * nums[i] - 1
            sums[i] = last
            dmap[last] = max(dmap[last], i)
        ans = 0
        for i, m in enumerate(sums):
            if m == 0:
                ans = max(ans, i + 1)
            else:
                ans = max(ans, dmap[m] - i)
        return ans


class Solution3:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        dmap = {0 : -1}
        ans = total = 0
        for i, n in enumerate(nums):
            total += 2 * nums[i] - 1
            if total in dmap:
                ans = max(ans, i - dmap[total])
            else:
                dmap[total] = i
        return ans