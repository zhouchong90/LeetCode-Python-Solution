class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
		
        #Hash Map to store the number and id
        m = {}
        for i,n in enumerate(nums,1):
            if (target - n) in m:
                return [m[target-n],i]
            else:
                m[n] = i
        return []
