class B:
    def palindrome(self,x):
        if x<0:
            print(x,"is not palindrome")  
        reverse = 0
        xb = x   
        while x>0:
            reverse = (reverse*10)+(x%10) 
            x //= 10 
        if reverse == xb:
                print(reverse,"Is palindrome")
        else:
                print(reverse,"is not Palindrome")
            
        

ob = B()
y = 11
ob.palindrome(y)
