class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic, res, start = {},0,0
        for i, ch in enumerate(s):
            if ch in dic:
                res = max(res, i-start)
                #we don't need to consider the string between the
                #repeated ones as its length cannot exceed max. consider for abba
                start = max(start,dic[ch]+1)
            #record the original ch
            dic[ch] = i
            #must consider last sequence
        return max(res,len(s)-start)