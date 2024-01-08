# CODE TO FIND THE 3 LARGEST ELEMENT IN ARRAY

import sys


 
def FindLargest_3(arr):
    n = len(arr)

    if n < 3 :
        print("Invalid Array size")

    first = second = third = -sys.maxsize

    for i in range(n):
        if arr[i] > first:
            third = second
            second = first
            first = arr[i]

        elif arr[i] > second:
            third = second
            second = arr[i]

        elif arr[i] > third:
            third = arr[i]

    print("Largest three elements are :",first, second , third)

    # COMPLEXITY
    # Time Complexity = O(N)

    # Another way to sort it in even more less time is by sorting the array and printing the last three elements

def findMax_3_Elements(arr):
        n = len(arr)
        arr = sorted(arr) # It will sort the array by tuned quick sort algorithm

        check = 0
        count = 0
        
        # To handle duplicates
        for i in range(1 , n + 1):
            if count < 3:
                if check != arr[n - i]:
                    print(arr[n - i],end = " ")
                    count += 1
                    check = arr[n - i]
                else:
                    break    



if __name__ == "__main__":
    arr = [64, 80, 21, 90, 78 , 52 , 12 , 59 , 101]
    FindLargest_3(arr)
    findMax_3_Elements(arr)


    

    
