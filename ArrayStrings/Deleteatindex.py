def deleteAtIndex(arr,size,index):

    i = index #1
    while(i<size-1): # 1 < 3
        arr[i] = arr[i+1]
        i+=1
    arr.pop()
    return size-1

arr = [10,20,30,40]
size = 4
index = 1
print(deleteAtIndex(arr,size,index))
print(arr)

# tc  = O(N)
# sc = O(1)