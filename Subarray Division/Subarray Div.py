def birthday(s, d, m):
    count=0
    for i in range(len(s)+1-m):
        if sum(s[i:i+m])==d:
            count+=1
    return count