class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        
        if x<0:
            return False
        
        ranger = 1
        while x/ranger >= 10:
            ranger*=10
        
        while x:
            left = x/ranger
            right = x%10
            if left!=right:
                return False
            else:
                x = (x%ranger)/10
                ranger/=100
        else:
            return True