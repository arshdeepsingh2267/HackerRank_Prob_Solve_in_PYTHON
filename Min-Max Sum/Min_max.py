def miniMaxSum(arr):
    maxi=0
    mini=0
    ma=sorted(arr,key=None,reverse=False)
    mi=sorted(arr,key=None,reverse=True)
    for i in range(len(arr)-1):
        maxi += ma[i]
        mini += mi[i]
    print(maxi,mini)