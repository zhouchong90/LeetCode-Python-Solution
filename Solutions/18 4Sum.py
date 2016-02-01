class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        num = sorted(nums)
        n = len(nums)
        m = collections.defaultdict(list)
        res = set()
        
        for i in xrange(n-1):
            for j in xrange(i+1,n):
                m[num[i]+num[j]].append((i,j))
        
        for i in xrange(n-1):
            for j in xrange(i+1,n):
                rest = target-num[i]-num[j]
                for pair in m[rest]:
                    if i>pair[1]:
                        res.add((num[pair[0]], num[pair[1]], num[i], num[j]))
        
        return list(res)