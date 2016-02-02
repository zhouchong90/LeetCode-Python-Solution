class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sl,pl = len(s), len(p)
        saves, savep = None,None
        si=pi=0
        while si < sl:
            
            if pi<pl and (p[pi]=="?" or s[si]==p[pi]):
                si+=1
                pi+=1
            elif pi<pl and p[pi]=="*":
                saves, savep = si,pi
                pi+=1
            elif savep is not None:#current matching failed
                si,pi = saves+1, savep
            else:# no match
                return False
        
        while pi<pl:
            if p[pi]!="*":
                return False
            pi+=1
        return True