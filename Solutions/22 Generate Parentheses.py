class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.helper("",n,n)
        return self.res
    
    def helper(self,current, left, right):
        if right == 0:
            self.res.append(current)
        else:
            if left>0:
                self.helper(current+"(", left-1, right)
            if left<right:
                self.helper(current+")", left, right-1)