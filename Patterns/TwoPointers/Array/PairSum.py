l = [0, 2, 3, 5, 8, 11]
target = 10

left = 0
right = len(l) - 1

while left < right:
    csum = l[left] + l[right]

    if csum == target:
        print([l[left], l[right]])  
        break                       
        
    elif csum < target:
        left += 1

    elif csum>target:
        right -= 1