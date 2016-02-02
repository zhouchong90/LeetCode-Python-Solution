class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        jump = nums[0]
        for i in range(1,len(nums)):
            if jump == 0:
                return False
            jump -= 1
            jump = max(jump,nums[i])
        return True
            