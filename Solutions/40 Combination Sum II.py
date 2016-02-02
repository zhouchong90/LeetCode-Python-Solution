class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.res = set()
        self.helper(candidates,target,0,tuple())
        
        return list(self.res)
    
    
    def helper(self,candidates, target, start, item):
        
        if target == 0:
            self.res.add(item)
        
        for i in xrange(start,len(candidates)):
            if target<candidates[i]:
                return
            
            self.helper(candidates,target-candidates[i], i+1, item+(candidates[i],) )
            