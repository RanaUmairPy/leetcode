def sort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr


arr = [1,2,7,4,9,10,-1,14,17]
print(sort(arr))