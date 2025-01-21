class A:
    def twosum(self,nums,t):
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n-1):
                for z in range(i+2,n):
                 if nums[i]+nums[j]+nums[z] == t:
                     print("The two numbers are: ",nums[i],nums[j],nums[z])
        
        return "No two sum solution"
ob = A()
y = 10
num = [1,3,5,6,4,20,-10]

print(ob.twosum(num,y))   