
def Romin(s):
    
    romin = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L' :0,
        'C' : 100,
        'D' : 500,
        'M' : 1000,       
    }
    
    res = 0
    
    for i in range(len(s)-1):
        if romin[s[i]]<romin[s[i+1]]:
            
            res -= romin[s[i]]
        else:
            res += romin[s[i]]
            
    print(res+romin[s[-1]])
    
x = "MMMMM"
Romin(x)