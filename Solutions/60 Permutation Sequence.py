class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        num = map(str,range(1,n+1))
        k-=1
        res = []
        base = math.factorial(n-1)
        for i in xrange(n-1, 0, -1):
            index,k = divmod(k,base)  
            base/=i
            res.append(num[index])
            num.pop(index)
        res.append((num[0]))
        return "".join(res)
            