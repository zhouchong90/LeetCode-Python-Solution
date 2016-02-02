class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxleft = [0 for i in xrange(len(height))]
        maxright = [0 for i in xrange(len(height))]
        ml = mr = 0
        for i in xrange(len(height)):
            ml = max(ml, height[i])
            maxleft[i] = ml
        for i in xrange(len(height)-1, -1, -1):
            mr = max(mr, height[i])
            maxright[i] = mr
        
        res = 0
        for i in xrange(len(height)):
            res += max( min(maxleft[i],maxright[i])-height[i], 0)
            
        return res