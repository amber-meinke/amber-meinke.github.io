# generic mergesort algorithm
def mergeSort(arr):

    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)
  
    
# merge 2 sorted lists into one big sorted list
def merge(L,R):

    newArr = []
    i = 0
    j = 0
    
    while i < len(L) and j < len(R):
        
        if L[i] < R[j]:
            newArr.append(L[i])
            i += 1
        else:
            newArr.append(R[j])
            j += 1
            
    # add any leftovers from the lists if one ran out first
    newArr += (L[i:])
    newArr += (R[j:])
    
    
    return newArr





userInput = input("Please enter a list of numbers ([x,y,z,...]): ")

li = []
for element in userInput:
    if element > '/' and element < ':': #only adding elements that have ascii values of digits
        li.append(int(element))
        
new = mergeSort(li)

print(new)
            
            
            
            
           
            
            
            