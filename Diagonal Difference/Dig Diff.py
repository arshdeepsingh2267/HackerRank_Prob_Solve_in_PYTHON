def diagonalDifference(arr):
    diag1=0
    diag2=0
    n=len(arr)
    for i in range(n):
        diag1+=arr[i][i]
        diag2 += arr[i][n-1-i]  #so that we can get the second diagonal. Maths :)
    return abs(diag1-diag2)