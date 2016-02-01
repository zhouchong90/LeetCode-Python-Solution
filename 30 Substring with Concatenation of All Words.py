class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        m,n,k = len(s), len(words), len(words[0])
        counter = collections.Counter(words)
        for i in xrange(k):
            temp = copy.deepcopy(counter)
            start = i
            for j in xrange(start, m-k+1, k):
                word = s[j:j+k]
                temp[word]-=1
                while temp[word] < 0:
                    temp[s[start:start+k]]+=1
                    start+=k
                if j+k-start==n*k:
                    res.append(start)
        return res