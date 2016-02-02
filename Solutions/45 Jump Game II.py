class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_max_distance = 0
        jumps = 0
        max_index = 0
        for i in range(len(nums)-1):
            max_index = max(max_index, i+nums[i])
            if current_max_distance == i:
                current_max_distance = max_index
                if current_max_distance>i:
                    jumps+=1
                else:
                    return -1
        return jumps
                