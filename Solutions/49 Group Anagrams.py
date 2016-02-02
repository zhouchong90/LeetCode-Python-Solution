from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
    
        a = defaultdict(list)
        for item in strs:
            a["".join(sorted(item))].append(item)
        
        res = []
        for v in a.itervalues():
            res.append(sorted(v))
        return res