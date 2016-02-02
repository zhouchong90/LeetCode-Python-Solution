class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def check(i,j):
            for k in xrange(i):
                if board[k]==j or abs(i-k) == abs(j-board[k]):
                    return False
            return True
        
        def dfs(i):
            if i == n:
                res[0]+=1
                return
            for j in xrange(n):
                if check(i,j):
                    board[i]=j
                    dfs(i+1)
        res = [0]
        board = [-1]*n
        dfs(0)
        return res[0]