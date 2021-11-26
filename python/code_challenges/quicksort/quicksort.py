"""
write a function that called QuickSort that
take aray of integer numbers
and return  sorted  array of integers

"""

def QuickSort(arr, left,right):

    if left < right :

        position_pivot = Partition(arr,left, right)

        QuickSort(arr, left, position_pivot - 1)

        QuickSort(arr, position_pivot + 1, right)

    return(arr)
    
def swap(arr , i , low):
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp


def Partition(arr, left,right):

    pivot = arr[right]

    low = left - 1

    for i in range(left,right) :

        if arr[i] <= pivot:

            low +=1

            swap(arr, i, low)

    swap(arr, right, low +1)

    return(low + 1)




