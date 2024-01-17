# BINARY SEARCH IN PYTHON

# Binary Search is defined as a searching algorithm used in a sorted array by repeatedly
# dividing the search interval in half. The idea of binary search is to use the information that the 
# array is sorted and reduce the time complexity to O(log N). 
 
# There are two types of Binary Search Algorithm

# 1. Iterative Binary Search Algorithm

def Iterative_BSearch(arr , low , high , val):
    while low <= high :
        
        mid = low + (high - low) // 2

        if arr[mid] == val:
            return mid
        
        elif arr[mid] < val:
            low = mid + 1

        elif arr[mid] > val:
            high = mid - 1

    return -1

# 2. Recursive Binary Search Algorithm

def Recursive_BSearch(arr , low , high , val):
    if low <= high:

        mid = low + (high - low) // 2

        if arr[mid] == val:
            return mid
        
        elif arr[mid] < val:
            return Recursive_BSearch(arr , mid + 1 , high , val)
        
        else:
            return Recursive_BSearch(arr , low , mid - 1 , val)


if __name__ == "__main__":
    arr = [12, 13 , 42 , 45 , 47 , 53 , 58 , 65 , 69]
    val = 45

    result = Iterative_BSearch(arr , 0 , len(arr) - 1 , val)
    result1 = Recursive_BSearch(arr , 0 , len(arr) - 1 , val)

    if result == -1:
        print("The value in not in the array")

    else:
        print("The value is at position" , result)
        print("THE VALUE AT POSIITON :",result1)     


# COMPLEXITY
        # The time complexity of binary search algorithm is O(log n).
        # BEST CASE = O(1)
        # WORST CASE = O(logN)
        # AVERAGE CASE = O(Log N)