def compareTriplets(a, b):
    score=[0,0]
    for i,j in zip(a,b):
        if i > j:
            score[0]+=1
        elif j > i:
            score[1]+=1
    return score
