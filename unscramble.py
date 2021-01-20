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


### start of program

letters = input("Please enter a character string (ex. 'abcdefg'): ")
letters += '\n'
matches = []
string = mergeSort(letters)

file = open("words.txt","r")
for line in file:
    tempLine = mergeSort(line)
    if tempLine == string:
        matches.append(line[:len(line)-1])
        
print("Possible words: ", matches)







