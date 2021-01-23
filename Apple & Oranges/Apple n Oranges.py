def countApplesAndOranges(s, t, a, b, apples, oranges):
    count=0
    count2=0
    for i in range(len(apples)):
        if apples[i]+a >=s and apples[i]+a<=t:
            count+=1
    print(count)
    
    for i in range(len(oranges)):
        if oranges[i]+b >=s and oranges[i]+b<=t:
            count2+=1
    print(count2)
