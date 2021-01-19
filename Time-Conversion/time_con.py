def timeConversion(s):
    #
    # Write your code here.
    pmc=int(s[0:2])
    if "PM" in s and pmc==12:
        return s[:-2]
    elif "PM" in s and pmc!=12:
        pmc=pmc+12
        news=s.replace(s[0:2],str(pmc))
        return news[:-2]
    elif "AM" in s and pmc==12:    
        pmc='00'
        newa=s.replace(s[0:2],str(pmc))
        return newa[:-2]    
    else:    
        return s[:-2] 
