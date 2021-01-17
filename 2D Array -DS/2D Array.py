def hourglassSum(arr):
    livar=[]
    var=0
    for i in range(0,4):
        for j in range(0,4):
            var=sum([arr[i][j],arr[i][j+1],arr[i][j+2],
                            arr[i+1][j+1],
                    arr[i+2][j],arr[i+2][j+1],arr[i+2][j+2]]) 
            livar.append(var)
    return max(livar)