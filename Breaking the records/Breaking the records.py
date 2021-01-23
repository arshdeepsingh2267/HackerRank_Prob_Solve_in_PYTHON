def breakingRecords(scores):
    valp=0
    valn=0
    mini=scores[0]
    maxi=scores[0]
    for i in scores:
        if i > maxi:
            maxi=i
            valp+=1
        if i<mini:
            mini=i
            valn+=1
    return (valp,valn)