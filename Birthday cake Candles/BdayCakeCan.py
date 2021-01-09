def birthdayCakeCandles(candles):
    # Write your code here
    count=0
    maxi=max(candles)
    for i in candles:
        if i==maxi:
            count+=1
    return count