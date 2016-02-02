class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        
        sums = maxs = nums[0]
        
        for i in range(1,len(nums)):
            sums = max(sums+nums[i],nums[i])# if the sum of subarray is less than current value, reset to current
            maxs = max(sums,maxs)
            
        return maxs