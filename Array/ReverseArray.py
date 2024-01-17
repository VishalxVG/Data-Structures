# Code to reverse a array

def ReverseArray(arr , start , end):
    while start < end :
        arr[start] , arr[end] = arr[end] , arr[start]
        start += 1
        end -= 1
    return arr
if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    print("Original Array is:",arr)
    print("After reversing array:",ReverseArray(arr , 0 , len(arr)-1))
