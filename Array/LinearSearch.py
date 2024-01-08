# LINEAR SEARCH In Python

def Lsearch(arr , N , val):
    for i in range(0 , N):
        if arr[i] == val:
            return i
    return -1

if __name__ == "__main__":
    arr = [5 , 6 , 7 , 8]
    N = len(arr)
    val = int(input("Enter a number :"))

    result = Lsearch(arr , N , val)

    if result == -1:
        print("The number doesnot exist")
    else:
        print("The number is at position :",result)