class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        
        res = ""
        
        res+=self.helper(num/1000,"","","","M")
        num%=1000
        res+=self.helper(num/100,"CM","D","CD","C")
        num%=100
        res+=self.helper(num/10,"XC","L","XL","X")
        num%=10
        res+=self.helper(num,"IX","V","IV","I")
        return res
        
    
    def helper(self,num, nine,five,four,one):
        res = ""
        if num==9:
            res+=nine
        else:
            if num>=5:
                res+=five
                num-=5
            if num==4:
                res+=four
            else:
                res+=one*num
            
        return res