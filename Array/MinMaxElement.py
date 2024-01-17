
# FINDING THE MINIMUM AND MAXIMUM ELEMENT IN THE ARRAY

def getMin(arr):
    minElement = arr[0]
    for i in range(len(arr)):
        minElement = min(minElement , arr[i])
    return minElement

def getMax(arr):
    maxElement = arr[0]
    for i in range(len(arr)):
        maxElement = max(maxElement , arr[i])
    return maxElement

if __name__ == "__main__":
    arr = [5 , 7 , 9 , 4 , 8 , 3 , 6 , 2] 
    print("Max Element:",getMax(arr))
    print("Min Element:",getMin(arr))   
