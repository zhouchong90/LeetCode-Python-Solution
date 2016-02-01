class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        if not haystack:
            return -1
            
        for i in range(len(haystack)-len(needle)+1):
            
            for j in range(len(needle)):
                
                if haystack[i+j]!=needle[j]:
                    break
            else:
                return i
        else:
            return -1