def search(arr,target):
    arr.sort()
    print(arr)
    l = 0
    r = len(arr)-1
    while l<=r:
        mid = (l+r)//2
        
        if arr[mid] == target:
            return mid
        elif arr[mid]>target:
            r = mid-1
        else:
            l = mid+1
    return -1
    

arr = [1,2,3,4,100,6,7,19,9,10]
target = 7
print(search(arr,target))