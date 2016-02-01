class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        self.m = [' ','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        self.res = []
        self.addLetter(digits, 0, "")
        return self.res

    def addLetter(self,digits, current,path):
        if current == len(digits):
            if path:
                self.res.append(path)
            return
        
        for i in self.m[int(digits[current])]:
            self.addLetter(digits, current+1, path+i)