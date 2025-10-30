def word_search(board,word):
    rows=len(board)
    cols=len(board[0])
    def dfs(r,c,i):
        if i==len(word):
            return True
        if r<0 or r>=rows or c<0 or c>=cols:
            return False
        if board[r][c]!=word[i]:
            return False
       
        temp=board[r][c]
        board[r][c]='#'
        res=(dfs(r+1,c,i+1) or
              dfs(r-1,c,i+1) or 
              dfs(r,c+1,i+1) or 
              dfs(r,c-1,i+1))
        board[r][c]=temp
        return res
    for i in range(rows):
        for j in range(cols):
            if board[i][j]==word[0] and dfs(i,j,0):
                return True
    return False
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
print(word_search(board,word))
    
