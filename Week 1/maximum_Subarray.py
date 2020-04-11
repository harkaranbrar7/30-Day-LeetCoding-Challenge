'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''
from typing import List

class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = res = nums[0]
        for i in range(1, len(nums)):
            dp = max(dp + nums[i], nums[i])
            if dp > res:
                res = dp
        
        return res

class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum

class Solution3:
    def maxSubArray(self, nums: List[int]) -> int:

        max_so_far = -maxint - 1
        max_ending_here = 0
        
        for i in range(0, size): 
            max_ending_here = max_ending_here + a[i] 
            if (max_so_far < max_ending_here): 
                max_so_far = max_ending_here 
    
            if max_ending_here < 0: 
                max_ending_here = 0   
        return max_so_far 

class Solution4:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            if nums[i-1]>0:
                nums[i]+=nums[i-1]
        return max(nums)

class Solution5:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = -(1<<31)
        temp = 0
        for num in nums:
            temp = temp + num
            if temp > max:
                max = temp
            if temp < 0:
                temp = 0
        return max

a = Solution1()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(a.maxSubArray([1,-2,3,-4]))
print(a.maxSubArray([]))
