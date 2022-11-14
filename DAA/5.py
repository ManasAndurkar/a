# Design n-Queens matrix having first Queen placed. Use backtracking to place remaining Queens to generate the final 8-queen’s matrix.


N = 8


b = [[0 for _ in range(N)] for _ in range(N)]


def safe(board , r ,c):
    for i in range(N):
        if board[r][i] == 1 or board[i][c] == 1:
            return False
    
    #  less than r , c 
    
    i,j = r,c 
    
    while(i>=0 and j>=0):
        if board[i][j] == 1:
            return False
        i = i-1
        j = j-1
    
    i,j = r,c  
    while(i<N and j < N):
        if board[i][j] == 1:
            return False
        i = i+1
        j = j+1
    i,j = r,c  
    while(i>=0 and j < N):
        if board[i][j] == 1:
            return False
        i = i-1
        j = j+1
    i,j = r,c  
    while(i<N and j>=0):
        if board[i][j] == 1:
            return False
        i = i+1
        j = j-1
    return True

b[0][1] = 1

    
# fixed_queen 


def queen(b , c = 1):
    if c >= N:
        return True
    for i in range(N):
        if safe(b , i , c):
            b[i][c] = 1 
            if queen(b , c+1):
                return True
            b[i][c] = 0
    return False

print(queen(b))

for i in b:
    print(i)
