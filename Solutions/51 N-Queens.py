class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        #check whether a queen can be placed in row i, column j
        def valid(i,j):
            for row in range(i):
                if board[row] == j or abs(row-i)==abs(board[row]-j):
                    return False
            return True
        
        def dfs(i,current_values):
            if i == n:
                res.append(current_values)
                return
            for j in xrange(n):
                if valid(i,j):
                    board[i] = j
                    dfs(i+1,current_values+[ "."*j+"Q"+"."*(n-j-1) ])
            
        board = [-1]*n # the j index of the queen placement at each row.
        res = []
        dfs(0,[])
        return res