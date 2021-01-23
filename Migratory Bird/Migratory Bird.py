def migratoryBirds(arr):
    invar=[0,0,0,0,0,0]
    for i in range(len(arr)):
        invar[arr[i]]+=1
    return invar.index(max(invar))