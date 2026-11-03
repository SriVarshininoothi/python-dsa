def insertValue(arr,size,index,value):


#Time complexity is O(n)
#Space complexity is O(1)


    arr.append(None)  #expand list in python
    i = size #5
    while(i>index): #5>1 ---- 1>1

        arr[i]=arr[i-1] # arr[5]=arr[4] => 50
        i=i-1 #decrease i to end
    arr[index] = value
    return size+1
    

arr = [10,20,30,40,50]
size=5
index=1
value=15
print(insertValue(arr,size,index,value))
print(arr)


